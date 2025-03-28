from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from common.models import Registration
from .forms import InnoxForm


class InnoxListView(ListView):
    model = Registration
    template_name = "panel/lid/list.html"
    context_object_name = "objects"
    queryset = Registration.objects.all().order_by("-id")
    paginate_by = 10
    
    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(full_name__icontains=search)

        return object_list
class InnoxCreateView(CreateView):
    model = Registration
    form_class = InnoxForm
    template_name = "panel/lid/create.html"
    context_object_name = "object"
    success_url = "panel:innox-list"
    success_create_url = "panel:innox-create"


class InnoxDeleteView(DeleteView):
    model = Registration
    success_url ="panel:innox-list"
    context_object_name = "object"


class InnoxUpdateView(UpdateView):
    model = Registration
    form_class = InnoxForm
    success_url ="panel:innox-list"
    context_object_name = "object"
    template_name = "panel/lid/create.html"
    success_create_url = "panel:innox-update"


