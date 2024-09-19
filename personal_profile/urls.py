from django.urls import path
from personal_profile import views

urlpatterns = [
    
    path('', views.profile, name = 'aboutme')
]