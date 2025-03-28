from django.urls import path
from .views import InnoxListView,InnoxCreateView,InnoxDeleteView,InnoxUpdateView



urlpatterns = [
        path("", InnoxListView.as_view(), name="innox-list"),
        path("create/", InnoxCreateView.as_view(), name="Innox-create"),
        path("delete/<pk>/", InnoxDeleteView.as_view(), name="Innox-delete"),
        path("update/<pk>/", InnoxUpdateView.as_view(), name="Innox-update"),


        ]
