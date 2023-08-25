from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from palette.models import Palette
from palette.serializers import *


class PaletteAPIView(APIView):
    
    permission_classes = [IsAuthenticated|AllowAny]

    def post(self, request):
        
        ##assign created by value by requisting user
        request.data['created_by'] = request.user.id
        serializer = PaletteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'data created', 'data': serializer.data,'status':status.HTTP_201_CREATED})
        else:
            return Response({'message': 'not okay', 'data': serializer.errors, 'status':status.HTTP_405_METHOD_NOT_ALLOWED})
    

    def get(self, request):

        ##geting only public palette
        get_public_palettes = Palette.objects.filter(is_public=True)
        serializer = PaletteSerializer(get_public_palettes, many=True).data
        if not serializer:            
            return Response({'message': 'no data', 'data': [], 'status':status.HTTP_404_NOT_FOUND})
        else:
            return Response({'message': 'showing data', 'data': serializer,'status':status.HTTP_200_OK})


class PublishPaletteAPIView(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        try:
            owner = request.user
            get_palette = Palette.objects.get(id=request.data['palette_id'])
            ##checking the owner of the palette 
            ##user can publish/private his own palette
            if owner == get_palette.created_by:
                get_palette.is_public = request.data['is_public']
                get_palette.save()
                return Response({'message': 'data updated', 'data': PaletteSerializer(get_palette).data,'status':status.HTTP_200_OK})
            return Response({'message': 'not allow', 'data': '','status':status.HTTP_405_METHOD_NOT_ALLOWED})

        except Exception as e:
            print(e)
            return Response({'message': 'not okay', 'data': str(e), 'status':status.HTTP_405_METHOD_NOT_ALLOWED})
    

class FavoritePaletteAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        try:
            get_palette = Palette.objects.get(id=request.data['palette'], is_public=True)
        except:
            return Response({'message': 'not found', 'data': '', 'status':status.HTTP_404_NOT_FOUND})

        ##checking other's palette
        if get_palette.created_by == request.user:
            return Response({'message': 'unable to add', 'data': '', 'status':status.HTTP_405_METHOD_NOT_ALLOWED})
        
        ##adding other's palette in database
        else:
            request.data['user'] = request.user.id
            serializer = FavoritePaletteSerializer(data=request.data)
            if serializer.is_valid():            
                serializer.save()
                return Response({'message': 'data created', 'data': serializer.data,'status':status.HTTP_201_CREATED})
            else:
                return Response({'message': 'not okay', 'data': serializer.errors, 'status':status.HTTP_405_METHOD_NOT_ALLOWED})
      

    def get(self, request):

        get_palettes = FavoritePalette.objects.filter(user=request.user.id)
        serializer   = FavoritePaletteSerializer(get_palettes, many=True).data

        if not serializer:
            return Response({'message': 'not found', 'data': '', 'status':status.HTTP_404_NOT_FOUND})
        else:
            return Response({'message': 'showing data ', 'data': serializer,'status':status.HTTP_200_OK})
     

class SearchAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        q = request.GET['q']
        results = Palette.objects.filter(name__contains=q)
        color = Color.objects.filter(color__contains=q)
        print(color)


        results = Palette.objects.filter(Q(name__contains=q, is_public=True) 
                                        | Q(dominant_color__color__contains=q) 
                                        | Q(accent_color__color__contains=q)

        )  
        if not results:
            return Response({'message': 'no shared file', 'data': [], 'status':status.HTTP_404_NOT_FOUND})
        results = results.values().distinct()
        return Response({'message': 'showing data', 'data': results,'status':status.HTTP_200_OK})

