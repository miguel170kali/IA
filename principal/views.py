from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings  # Importar la configuración para el email
from .forms import ContactoForm  # Importa tu formulario (si lo creaste)


# Página principal
def index(request):
    return render(request, 'index.html')

# Sección institucional
def resena(request):
    return render(request, 'resena.html')

def mision_vision_objetivos(request):
    return render(request, 'mision_vision_objetivos.html')

#Seccion de valores
def valores(request):
    return render(request, 'valores.html')

# Sección de servicios
def consultorias_en_IA(request):
    return render(request, 'consultorias_en_IA.html')

def cursos_cortos_IA(request):
    return render(request, 'cursos_cortos_IA.html')

def eventos_talleres(request):
    return render(request, 'eventos_talleres.html')

# Sección de contacto
def formulario_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)  # Asume que ya tienes un forms.py
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            mensaje = form.cleaned_data['mensaje']

            asunto = 'Nuevo mensaje de contacto desde ColombiaCreaIA'
            cuerpo = f"Nombre: {nombre}\nEmail: {email}\nTeléfono: {telefono}\nMensaje:\n{mensaje}"

            try:
                send_mail(
                    asunto,
                    cuerpo,
                    settings.EMAIL_HOST_USER,  # Usar la configuración de settings.py
                    [settings.RECIPIENT_EMAIL],  # Usar la configuración de settings.py
                    fail_silently=False,
                )
                return redirect('formulario_contacto_exito')  # Redirige por nombre de URL
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
                return render(request, 'formulario_contacto_error.html', {'error': str(e)})  # Renderiza una página de error
    else:
        form = ContactoForm()  # Inicializa el formulario vacío

    return render(request, 'formulario_contacto.html', {'form': form})

def informacion_contacto(request):
    return render(request, 'informacion_contacto.html')

def formulario_contacto_exito(request):  # Nueva vista para éxito
    return render(request, 'formulario_contacto_exito.html')

def formulario_contacto_error(request):  # Nueva vista para error
    return render(request, 'formulario_contacto_error.html')