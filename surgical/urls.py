from django.urls import path
from .views import Functions

#=============================================================================================================#
urlpatterns = [
   path('modules/', Functions.module_list, name='surgical'),
   #path('modules/units/', Functions.unit_list, name='units'),
   path('articles', Functions.article_list, name='surgical-articles'),
   path('journals', Functions.journal_list, name='surgical-journals'),
]