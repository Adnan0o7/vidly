from django.db import models
from tastypie.recources import ModelResource

class MovieResource(ModelResource):
  class Meta:
    queryset = Movie.objects.all()
    resource_name = 'movies'
