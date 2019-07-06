from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class UnitManager(models.Manager):
	def new_unit(self, unit):
		new_unit = self.create(unit=re.sub('\s+', '-', unit).lower())

		new_unit.save()
		return new_unit
#============================================================================================================================#

class Module(models.Model):
	objects = models.Manager()
	module_number = models.IntegerField(default=0)
	thumbnail = models.ImageField(
		upload_to='surgical/modules/thumbnails', null=True, 
		blank=True
	)
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True)
	updated =models.DateTimeField(auto_now=True, auto_now_add=False)
	slug = models.SlugField(unique=True, null=True)
	
	def create_slug(instance, new_slug=None):
		"""checks to see if the slug exists recursively."""
		slug = slugify(instance.title)
		if new_slug is not None:
			slug = new_slug
		qs = BasicData.objects.filter(slug=slug).order_by('-id')
		exists = qs.exists
		if exists:
			new_slug = "%s-%s" %(slug, qs.first().id)
			return create_slug(instance, new_slug=new_slug)
		return slug
		
	def get_absolute_url(self):
		return reverse(
			'module', 
			kwarg={'slug':self.slug, 'id':self.id}
			)
	
	def __int__(self):
		self.module_number
	
	class Meta:
		verbose_name = ("Module")
		verbose_name_plural = ("Modules")
#============================================================================================================================#

class Unit(models.Model):
	unit_number = models.IntegerField(default=0)
	thumbnail = models.ImageField(
		upload_to='surgical/modules/units/thumbnails', null=True, 
		blank=True
	)
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True)
	file_upload = models.FileField(upload_to='surgical/modules/units')
	module = models.ForeignKey(
		Module, null=True, 
		blank=True, verbose_name=("Module"), 
		on_delete=models.PROTECT
	)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	slug = models.SlugField(unique=True, null=True)
	
	def create_slug(instance, new_slug=None):
		"""checks to see if the slug exists recursively."""
		slug = slugify(instance.title)
		if new_slug is not None:
			slug = new_slug
		qs = BasicData.objects.filter(slug=slug).order_by('-id')
		exists = qs.exists
		if exists:
			new_slug = "%s-%s" %(slug, qs.first().id)
			return create_slug(instance, new_slug=new_slug)
		return slug
		
	def get_absolute_url(self):
		return reverse(
			'module', 
			kwarg={'slug':self.slug, 'id':self.id}
			)
	
	def __int__(self):
		return self.unit_number
	
	class Meta:
		ordering = ('unit_number', 'title', 'description', 'updated')
		verbose_name = ("Unit")
		verbose_name_plural = ("Units")
#============================================================================================================================#

class BasicData(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	website= models.URLField(max_length=250, null=True)
	unit = models.ForeignKey(
		Unit, null=True, 
		blank=True, verbose_name=("Unit"), 
		on_delete=models.PROTECT
	)
	slug = models.SlugField(unique=True, null=True)
	
	def __str__(self):
		return self.title
	
	def create_slug(instance, new_slug=None):
		"""checks to see if the slug exists recursively."""
		slug = slugify(instance.title)
		if new_slug is not None:
			slug = new_slug
		qs = BasicData.objects.filter(slug=slug).order_by('-id')
		exists = qs.exists
		if exists:
			new_slug = "%s-%s" %(slug, qs.first().id)
			return create_slug(instance, new_slug=new_slug)
		return slug
		
	def get_absolute_url(self):
		return reverse(
			'module', 
			kwarg={'slug':self.slug, 'id':self.id}
			)
#============================================================================================================================#		

class Article(BasicData):
	file_upload = models.FileField(upload_to='surgical/articles', null=True)
	thumbnail = models.ImageField(upload_to='surgical/articles/thumbnails', 
		null=True, blank=True
	)
		
	class Meta:
		ordering = ('title', 'description', 'updated')
		verbose_name = ("Article")
		verbose_name_plural = ("Articles")
#============================================================================================================================#
		
class Journal(BasicData):
	file_upload = models.FileField(upload_to='surgical/journals', null=True)
	thumbnail = models.ImageField(upload_to='surgical/journals/thumbnails', 
		null=True, blank=True
	)
	
	class Meta:
		ordering = ('title', 'description', 'updated')
		verbose_name = ("Journal")
		verbose_name_plural = ("Journals")