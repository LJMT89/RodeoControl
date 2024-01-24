from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from datetime import datetime
from app_core.models import Finca, Rodeo, Animal

def index(request):
  rodeos = Rodeo.objects.all()

  context = {
    'rodeos':rodeos,
  }

  if request.method == 'POST':
    nombre = request.POST.get('nombre', '')
    descripcion = request.POST.get('descripcion', '')

    finca = Finca.objects.all().first()
    fecha_actual = datetime.now()
    Rodeo.objects.create(finca=finca, nombre=nombre, fecha=fecha_actual, descripcion=descripcion)
    
    return redirect(reverse('app_core:index'), context)

  return render(request, 'app_core/general/index.html', context)

def rodeo(request, pk):
  rodeo = get_object_or_404(Rodeo, pk=pk)
  animales = Animal.objects.filter(rodeo=pk)

  context = {
    'rodeo':rodeo,
    'animales':animales,
  }

  if request.method == 'POST':
    nombre_rodeo = request.POST.get('nombre_rodeo', '')
    descripcion_rodeo = request.POST.get('descripcion_rodeo', '')
    numero = request.POST.get('numero', '')
    fecha = request.POST.get('fecha', '')
    observacion = request.POST.get('observacion', '')
    animal_id = request.POST.get('animal_id', '')
    add_or_edit_or_delete = request.POST.get('add_or_edit_or_delete', '')

    if add_or_edit_or_delete == '0':
      Animal.objects.create(rodeo=rodeo, numero=numero, fecha=fecha, observacion=observacion)
    elif add_or_edit_or_delete == '1':
      Animal.objects.filter(pk=animal_id).update(rodeo=rodeo, numero=numero, fecha=fecha, observacion=observacion)
    elif add_or_edit_or_delete == '2':
      Animal.objects.filter(pk=animal_id).delete()
    elif add_or_edit_or_delete == '3':
      Rodeo.objects.filter(pk=pk).update(nombre=nombre_rodeo, descripcion=descripcion_rodeo)
    elif add_or_edit_or_delete == '4':
      Rodeo.objects.filter(pk=pk).delete()
      rodeos = Rodeo.objects.all()
      context = {
        'rodeos':rodeos,
      }
      return redirect(reverse('app_core:index'), context)
    
    return redirect(reverse('app_core:rodeo', args=[rodeo.id]), context)
  
  return render(request, 'app_core/general/rodeo.html', context)