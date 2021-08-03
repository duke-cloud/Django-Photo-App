from django.urls import path
from . import views


urlpatterns=[
    path('',views.gallery,name='gallery'),
    path('pix/<str:pk>/',views.viewPix,name='pix'),
    path('add/',views.addPix,name='add'),
]