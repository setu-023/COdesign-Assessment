from enum import unique
from django.db import models
from django.contrib.auth.models import User


class Color(models.Model):

    color = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True,null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.color


class Palette(models.Model):

    name  = models.CharField(max_length=255, unique=True)
    dominant_color = models.ManyToManyField(Color, related_name="d_color")
    accent_color = models.ManyToManyField(Color, related_name="a_color")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True,null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.name


class FavoritePalette(models.Model):
    
    palette = models.ForeignKey(Palette, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True, null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        unique_together = [["palette", "user"]]