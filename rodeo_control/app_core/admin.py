from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from app_core.resources import RodeoResource, AnimalResource
from app_core.models import Finca, Rodeo, Animal

class RodeoAdmin(ImportExportModelAdmin):
  resource_class = RodeoResource

class AnimalAdmin(ImportExportModelAdmin):
  resource_class = AnimalResource

admin.site.register(Finca)
admin.site.register(Rodeo, RodeoAdmin)
admin.site.register(Animal, AnimalAdmin)