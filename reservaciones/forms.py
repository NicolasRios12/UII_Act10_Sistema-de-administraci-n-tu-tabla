from django import forms
from .models import reservaciones


class reservacionesform(forms.ModelForm):
  class Meta:
    model = reservaciones
    fields = ['id_cliente', 'telefono', 'fecha_reserva', 'hora_reserva', 'num_personas']
    labels = {
      'id_cliente': 'id del cliente',
      'telefono': 'telefono',
      'fecha_reserva': 'fecha de la reservacion',
      'hora_reserva': 'hora de la reservacion',
      'num_personas': 'Numero de personas',
    }
    widgets = {
      'id_cliente': forms.NumberInput(attrs={'class': 'form-control'}),
      'telefono': forms.TextInput(attrs={'class': 'form-control'}),
      'fecha_reserva': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'hora_reserva': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
      'num_personas': forms.NumberInput(attrs={'class': 'form-control'}),
    }
