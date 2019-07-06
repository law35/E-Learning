from django.urls import path
from .views import Functions

urlpatterns = [
	path('modules/', Functions.module_list, name='biology'),
	path('modules/units/cells', Functions.unit_list, name='units'),
	path('articles', Functions.article_list, name='biology-articles'),
	path('journals', Functions.journal_list, name='biology-journals'),
   #path('<slug:slug>,<int:id>', ),
]