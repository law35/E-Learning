from django.shortcuts import render
from django.http import HttpResponse

#=========================================================================================================================#

class NewsUpdates():
	def news(request):
		return render(request, 'news.html')
