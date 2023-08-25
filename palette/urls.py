from django.urls import path
from .views import *

urlpatterns = [
    
    path('', PaletteAPIView.as_view()),
    path('publish/', PublishPaletteAPIView.as_view()),
    path('favorite/', FavoritePaletteAPIView.as_view()),
    path('search/', SearchAPI.as_view())

]
