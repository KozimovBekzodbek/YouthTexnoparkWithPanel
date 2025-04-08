from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, View):  
    login_url = '/login/'  

    def get(self, request):
        return render(request, "panel/index.html")
