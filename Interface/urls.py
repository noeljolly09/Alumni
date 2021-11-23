
from django.contrib import admin
from django.urls import path
from django.conf.urls import include




from . import views


from .views import *
from  accounts import views as account_views



urlpatterns = [
   path('', views.home, name='homepage'),

   path('userprofile',views.Profile,name='userprofile'),
   
   #alumni part
   path('alumniDirectory', Alumnidirectory.as_view(), name= 'alumnidirectory'),
   path('alumniDirectory/alumni/<int:pk>', MyProfile.as_view(), name= 'alumniprofile'),
   path('alumniDirectory/alumni/add', AddAlumni.as_view(), name='alumniadd'),
   path('alumniDirectory/alumni/Updateprofile/<int:pk>',UpdateProfile.as_view(), name='updateprofile'),


   #gallery part
   path('Gallery' ,GalleryImages.as_view(), name='gallery'),
   path('Gallery/add' ,AddImagesGallery.as_view(), name='gallery_add'),


]

