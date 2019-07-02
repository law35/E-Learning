from django.urls import path
# from home.newsfeed import LatestNews
from . import views

urlpatterns = [
   path('', views.HomePage.homePage, name='home'),
]