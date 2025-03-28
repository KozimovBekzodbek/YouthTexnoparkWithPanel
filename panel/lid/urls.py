from django.urls import path
from .views import (
    CourseContactListView,
    CourseContactCreateView,
    CourseContactDeleteView,
    CourseContactUpdateView,
)

urlpatterns = [
    path("", CourseContactListView.as_view(), name="coursecontact-list"),
    path("create/", CourseContactCreateView.as_view(), name="coursecontact-create"),
    path("delete/<pk>/", CourseContactDeleteView.as_view(), name="coursecontact-delete"),
    path("update/<pk>/", CourseContactUpdateView.as_view(), name="coursecontact-update"),
]
