from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Page
from .forms import PageForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page
    
@method_decorator(staff_member_required, name='dispatch')    
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    
    """
    def get_success_url(self):
        return reverse('pages:pages')    
    """
    success_url = reverse_lazy('pages:pages') # Se puede utilizar tanto el def_get_success_url como el success_url con reverse_lazy
    

@method_decorator(staff_member_required, name='dispatch') 
class PageUpdateView(StaffRequiredMixin ,UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + "?ok"
 
@method_decorator(staff_member_required, name='dispatch')    
class PageDeleteView(StaffRequiredMixin ,DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')