from django.shortcuts import render
from django.http import HttpResponse

#===============================================================================================================================#

class HomePage():
	def homePage(request):
		return render(request, 'home.html')