from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from common.models import ServiceContact
from .forms import ServiceContactForm
from django.contrib.auth.mixins import LoginRequiredMixin




class ServiceContactListView(LoginRequiredMixin,ListView):
    model = ServiceContact
    template_name = "panel/serivice/list.html"
    context_object_name = "objects"
    queryset = ServiceContact.objects.all().order_by("-id")
    paginate_by = 10
    login_url = '/login/'

    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(name__icontains=search)

        return object_list

class ServiceContactCreateView(LoginRequiredMixin,CreateView):
    model = ServiceContact
    form_class = ServiceContactForm
    template_name = "panel/serivice/create.html"
    context_object_name = "object"
    success_url = "panel:servicecontact-list"
    success_create_url = "panel:servicecontact-create"
    login_url = '/login/'

class ServiceContactDeleteView(LoginRequiredMixin,DeleteView):
    model = ServiceContact
    success_url = "panel:servicecontact-list"
    context_object_name = "object"
    login_url = '/login/'

class ServiceContactUpdateView(LoginRequiredMixin,UpdateView):
    model = ServiceContact
    form_class = ServiceContactForm
    template_name = "panel/serivice/create.html"
    context_object_name = "object"
    success_url = "panel:servicecontact-list"
    success_create_url = "panel:servicecontact-update"
    login_url = '/login/'
