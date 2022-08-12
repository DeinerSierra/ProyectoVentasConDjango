from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.messages import constants as messages
import json

from .models import Proveedor
from cmp.forms import ProveedorForm

# Create your views here.
class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
    
class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_list")
    login_url = 'bases:login'
    
    def form_valid(self, form):
        form.instance.usuarioCreador = self.request.user
        return super().form_valid(form)
    
class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_list")
    login_url = 'bases:login'
    
    def form_valid(self, form):
        form.instance.usuarioModificador = self.request.user.id
        return super().form_valid(form)

def inactivar_proveedor(request, id):
    template_name = 'cmp/inactivar_prov.html'
    contexto = {}
    proveedor = Proveedor.objects.filter(pk=id).first()
    
    if not proveedor:
        return HttpResponse('Proveedor no existe'+ str(id))
    if request.method == 'GET':
        contexto = {'obj':proveedor}
    
    if request.method == 'POST':
        proveedor.estado = False
        proveedor.save()
        contexto = {'obj':'OK'}
        return HttpResponse('Proveedor Inactivado')
    
    return render(request, template_name, contexto)
    
