from django.urls import path
from . import views
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('', views.PaginawebView.as_view(), name='index'),
    path('portafolios/', views.PortafolioView.as_view(), name='portafolios'),
    path('create/', views.ProyectoCreate.as_view(), name='create'),
    path('delete/<int:id>', views.deleteProyecto, name='delete'),
    path('logout/', logout_then_login, name='logout')
]