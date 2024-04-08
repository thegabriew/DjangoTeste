from django.urls import path
from . import views

urlpatterns = [
    path('/',views.index,name="index"),
    path("nome",views.nome, name = "nome"),
    path("kanye",views.kanye, name="kanye")
    
]