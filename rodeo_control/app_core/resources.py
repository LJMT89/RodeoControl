from import_export import resources
from app_core.models import Rodeo, Animal

class RodeoResource(resources.ModelResource):
   class Meta:
      model = Rodeo

class AnimalResource(resources.ModelResource):
   class Meta:
      model = Animal