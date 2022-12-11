from django.shortcuts import render, redirect
from .models import Proyecto
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from paginaweb.forms import ProyectoForm

# Create your views here.


class PaginawebView(TemplateView):
    template_name = "paginaweb/index.html"
    #extra_context = { "proyectos": Proyecto.objects.all() }


class PortafolioView(TemplateView):
    template_name = "paginaweb/portafolios.html"
    extra_context = { "proyectos": Proyecto.objects.all() }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proyectos"] = Proyecto.objects.all()
        return context



class ProyectoCreate(LoginRequiredMixin, FormView):
    model = Proyecto
    template_name = "paginaweb/create.html"
    form_class = ProyectoForm

    def form_valid(self, form):
        Proyecto.objects.create(**form.cleaned_data)
        return redirect("portafolios")

@login_required
def deleteProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect("portafolios")

