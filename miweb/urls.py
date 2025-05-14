from django.contrib import admin
from django.urls import path
from principal import views  # Asegúrate de que "principal" sea el nombre correcto de tu app

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),

    # Institucional
    path('resena/', views.resena, name='resena'),
    path('mision-vision-objetivos/', views.mision_vision_objetivos, name='mision_vision_objetivos'),
    path('valores/', views.valores, name='valores'),

    # Servicios
    path('cursos/', views.cursos_cortos_IA, name='cursos_cortos_IA'),  # Corregido
    path('consultorias/', views.consultorias_en_IA, name='consultorias_en_IA'),  # Corregido
    path('eventos/', views.eventos_talleres, name='eventos_talleres'),  # Corregido

    # Contacto
    path('formulario/', views.formulario_contacto, name='formulario_contacto'),  # Corregido
    path('informacion/', views.informacion_contacto, name='informacion_contacto'),  # Corregido
    path('formulario/exito/', views.formulario_contacto_exito, name='formulario_contacto_exito'), # URLs para éxito y error
    path('formulario/error/', views.formulario_contacto_error, name='formulario_contacto_error'),

    # Admin
    path('admin/', admin.site.urls),
]

# Personalización del panel de administración
admin.site.site_header = "Administración ColombiaCreaIA"
admin.site.site_title = "Admin ColombiaCreaIA"
admin.site.index_title = "Bienvenido al panel de administración"