from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import reservaciones
from .forms import reservacionesform


# Create your views here.
def index(request):
  return render(request, 'reservaciones/index.html', {
    'reservaciones': reservaciones.objects.all()
  })


def view_reservaciones(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = reservacionesform(request.POST)
    if form.is_valid():
        new_id_cliente = form.cleaned_data['id_cliente']
        new_telefono = form.cleaned_data['telefono']
        new_fecha_reserva = form.cleaned_data['fecha_reserva']
        new_hora_reserva = form.cleaned_data['hora_reserva']
        new_num_personas = form.cleaned_data['num_personas']

    nueva_reservacion = reservaciones(
        id_cliente=new_id_cliente,
        telefono=new_telefono,
        fecha_reserva=new_fecha_reserva,
        hora_reserva=new_hora_reserva,
        num_personas=new_num_personas
      )
    nueva_reservacion.save()
    return render(request, 'reservaciones/add.html', {
        'form': reservacionesform(),
        'success': True
      })
  else:
    form = reservacionesform()
  return render(request, 'reservaciones/add.html', {
    'form': reservacionesform()
  })


def edit(request, id):
  if request.method == 'POST':
    reservacion = reservaciones.objects.get(pk=id)
    form = reservacionesform(request.POST, instance=reservacion)
    if form.is_valid():
      form.save()
      return render(request, 'reservaciones/edit.html', {
        'form': form,
        'success': True
      })
  else:
    reservacion = reservaciones.objects.get(pk=id)
    form = reservacionesform(instance=reservacion)
  return render(request, 'reservaciones/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    reservacion = reservaciones.objects.get(pk=id)
    reservacion.delete()
  return HttpResponseRedirect(reverse('index'))
