from django.urls import include,path

from saludo import views

app_name ="saludo"

urlpatterns = [
    
    path('',  views.saludo, name='saludo'),
    path('consulta/', views.consulta, name='consulta')
   
    
]