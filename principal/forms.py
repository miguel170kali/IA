from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Tu nombre'}))
    email = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'placeholder': 'Tu correo'}))
    telefono = forms.CharField(label='Teléfono (Opcional)', required=False, widget=forms.TextInput(attrs={'placeholder': 'Tu teléfono (opcional)'}))
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu mensaje aquí'}))