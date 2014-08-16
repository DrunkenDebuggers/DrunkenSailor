from django.shortcuts import render
from django.http import HttpResponse
from sailor.models import Project
from django.template import RequestContext, loader
from django.views import generic

class IndexView(generic.ListView):
	template_name="sailor/index.html"
	context_object_name = 'projects'

	def get_queryset(self):
		return Project.objects.all()

class DetailView(generic.DetailView):
	model=Project
	template_name="sailor/project_detail.html"