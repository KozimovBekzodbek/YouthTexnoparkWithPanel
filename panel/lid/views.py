from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from common.models import CourseContact
from .forms import CourseContactForm
from django.contrib.auth.mixins import LoginRequiredMixin




class CourseContactListView(LoginRequiredMixin,ListView):
    model = CourseContact
    template_name = "panel/course/list.html"
    context_object_name = "objects"
    queryset = CourseContact.objects.all().order_by("-id")
    paginate_by = 10
    login_url = '/login/'

    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(name__icontains=search)

        return object_list

class CourseContactCreateView(LoginRequiredMixin,CreateView):
    model = CourseContact
    form_class = CourseContactForm
    template_name = "panel/course/create.html"
    context_object_name = "object"
    success_url = "panel:coursecontact-list"
    success_create_url = "panel:coursecontact-create"
    login_url = '/login/'

class CourseContactDeleteView(LoginRequiredMixin,DeleteView):
    model = CourseContact
    success_url = "panel:coursecontact-list"
    context_object_name = "object"
    login_url = '/login/'

class CourseContactUpdateView(LoginRequiredMixin,UpdateView):
    model = CourseContact
    form_class = CourseContactForm
    template_name = "panel/course/create.html"
    context_object_name = "object"
    success_url = "panel:coursecontact-list"
    success_create_url = "panel:coursecontact-update"
    login_url = '/login/'
