from django.contrib import admin
from .models import Unit, Module, Article, Journal

# Register your models here.

class UnitAdmin(admin.ModelAdmin):
	list_display = [
		'unit_number', 'title', 
		'description', 'updated'
	]
	
	list_display_links = ['title']
	
	class Meta:
		model = Unit


class ModuleAdmin(admin.ModelAdmin):
	list_display = [
		'module_number', 'title', 
		'description', 'updated', 
	]
	list_display_links = ['title']
	
	class Meta:
		model = Module
#==========================================================================================================================#
	
class ArticleAdmin(admin.ModelAdmin):
	list_display = [
		'title', 'description',
		'updated',
	]
	list_display_links = ['title']
	
	class Meta:
		model = Article


class JournalAdmin(admin.ModelAdmin):
	list_display = [
		'title', 'description',
		'updated',
	]
	list_display_links = ['title']
	
	class Meta:
		model = Journal

	
admin.site.register(Unit, UnitAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Journal, JournalAdmin)