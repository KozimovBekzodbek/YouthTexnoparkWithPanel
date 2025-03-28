from django.urls import path
from common import views
app_name = "common"


urlpatterns = [
        path("", views.HomeView.as_view(), name="home"),
        path("success/", views.SuccessView.as_view(), name="success"),
        path("error/", views.ErrorView.as_view(), name="error"),
        path("forms/", views.FormView.as_view(), name="forms"),
        path("courses/", views.CourseView.as_view(), name="courses"),
        path("service/", views.ServiceView.as_view(), name="service"),
]
