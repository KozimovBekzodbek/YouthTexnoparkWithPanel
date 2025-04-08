from django.urls import path
from .views import (
   ServiceContactListView,
   ServiceContactCreateView,
   ServiceContactDeleteView,
   ServiceContactUpdateView,
)

urlpatterns = [
    path("", ServiceContactListView.as_view(), name="servicecontact-list"),
    path("create/", ServiceContactCreateView.as_view(), name="servicecontact-create"),
    path("delete/<pk>/", ServiceContactDeleteView.as_view(), name="servicecontact-delete"),
    path("update/<pk>/", ServiceContactUpdateView.as_view(), name="servicecontact-update"),
]
