from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Module, Unit, Article, Journal
from django.template import loader
from django.http import HttpResponse

#===============================================================================================================================#

class Functions():	
	def module_list(request):
		"""List all module uploads"""
		object_list = Module.objects.all()
		paginator = Paginator(object_list, 1)
		page = request.GET.get('page')
		context = {'section': 'modules', 'object_list': object_list,}
		try:
			object_list = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer deliver the first page
			object_list = paginator.page(1)
		except EmptyPage:
			if request.is_ajax():
				# If the request is AJAX and the page is out of range return an empty page
				return HttpResponse('')
			# If page is out of range deliver last page of results
			object_list = paginator.page(paginator.num_pages)
		if request.is_ajax():
			return render(request, 'surgical_modules.html', context)	
		return render(request, 'surgical_modules.html', context)
		
	def unit_list(request):
		"""List all unit uploads"""
		object_list = Unit.objects.all()
		paginator = Paginator(object_list, 1)
		page = request.GET.get('page')
		context = {'section': 'units', "object_list": object_list,}
		try:
			object_list = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer deliver the first page
			object_list = paginator.page(1)
		except EmptyPage:
			if request.is_ajax():
				# If the request is AJAX and the page is out of range return an empty page
				return HttpResponse('')
			# If page is out of range deliver last page of results
			object_list = paginator.page(paginator.num_pages)
		if request.is_ajax():
			return render(request, 'cells.html', context)
		return render(request, 'cells.html', context)
		
	def article_list(request):
		"""List all articles"""
		object_list = Article.objects.all()
		paginator = Paginator(object_list, 1)
		page = request.GET.get('page')
		context = {'section': 'articles', "object_list": object_list,}
		try:
			object_list = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer deliver the first page
			object_list = paginator.page(1)
		except EmptyPage:
			if request.is_ajax():
				# If the request is AJAX and the page is out of range return an empty page
				return HttpResponse('')
			# If page is out of range deliver last page of results
			object_list = paginator.page(paginator.num_pages)
		if request.is_ajax():
			return render(request, 'surgical_articles.html', context)
		return render(request, 'surgical_articles.html', context)
		
	def journal_list(request):
		"""List all journals"""
		object_list = Journal.objects.all()
		paginator = Paginator(object_list, 1)
		page = request.GET.get('page')
		context = {'section': 'journals', "object_list": object_list,}
		try:
			object_list = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer deliver the first page
			object_list = paginator.page(1)
		except EmptyPage:
			if request.is_ajax():
				# If the request is AJAX and the page is out of range return an empty page
				return HttpResponse('')
			# If page is out of range deliver last page of results
			object_list = paginator.page(paginator.num_pages)
		if request.is_ajax():
			return render(request, 'surgical_journals.html', context)
		return render(request, 'surgical_journals.html', context)