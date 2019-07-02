from django.urls import path
# from home.newsfeed import LatestNews
from .views import NewsUpdates

urlpatterns = [
   path('', NewsUpdates.news, name='breaking-news'),
   path('home/', NewsUpdates.homePage, name='home'),
]