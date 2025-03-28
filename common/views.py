from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import  messages
from common import models
import traceback
from django.shortcuts import render, redirect
import os
from django.http import FileResponse, Http404
from django.conf import settings





class HomeView(View):
    def get(self, request):
        main = models.MainPage.objects.all().order_by("-id")
        innox = models.InnoX.objects.all().order_by("-id")
        aboutus = models.AboutUs.objects.all().order_by("-id")
        mentors = models.Mentors.objects.all().order_by("-id")
        news = models.News.objects.all().order_by("-id")
        whytexnopark = models.WhyTexnopark.objects.all().order_by("-id")
        studentproject = models.StudentProject.objects.all().order_by("-id")
        question = models.Question.objects.filter(is_top=True).order_by("-id")
        sliderimages = models.SliderContent.objects.all().order_by("-id")
        slidercompany = models.SliderCompany.objects.all().order_by("-id")
        footer = models.Footer.objects.all()
        major = models.Course.objects.values_list('name', flat=True)


        context = {
            'main' : main,
            'innox' : innox,
            'aboutus': aboutus,
            'mentors' : mentors,
            'news': news,
            'whytexnopark':whytexnopark,
            'studentproject': studentproject,
            'question': question,
            'sliderimages':sliderimages,
            'slidercompany':slidercompany,
            'major': major,
            'footer':footer,
        }
        
        return render(request, "index.html", context)
    def post(self, request):
        print("++++++++++++++GOOOD+++++++++++++++++++++++++++")
        data = {
            "name": request.POST.get("name"),
            "major": request.POST.get("major"),  
            "age": request.POST.get("age"),
            "phone_number": request.POST.get("phone_number"),
        }
        print("Data received from POST request:", data)

        try:
            major_instance = get_object_or_404(models.Course, name=data["major"])  
            registration = models.CourseContact(
                name=data["name"],
                major=major_instance,  
                age=data["age"],
                phone_number=data["phone_number"],
            )
            registration.save()

            messages.success(request, 'Your message has been sent successfully!')
            return redirect("common:success")

        except Exception as e:
            print("Error occurred:", str(e))
            traceback.print_exc()
            messages.error(request, f'An error occurred: {str(e)}')  
            return redirect("common:error")


class SuccessView(View):
    def get(self, request):

        return render(request, "success.html")

class ErrorView(View):
    def get(self, request):

        return render(request, "error.html")



class FormView(View):
    def get(self, request):
        skill1 = models.StartAppCategory.objects.all()
        skill2 = models.Purposes.objects.all()
        
        context = {
            "skill1": skill1,
            "skill2": skill2,
        }
        return render(request, "forms.html", context)

    def post(self, request):
        print("++++++++++++++GOOOD+++++++++++++++++++++++++++")
        agree = request.POST.get("agree") == "True"

        data = {
            "name": request.POST.get("name"),
            "gender": request.POST.get("gender"),  # Fixed gender extraction
            "date": request.POST.get("date"),
            "address": request.POST.get("address"),
            "phonenumber": request.POST.get("phonenumber"),
            "startappname": request.POST.get("startappname"),
            "skills": request.POST.getlist("skills"),
            "anotherskill": request.POST.get("anotherskill"),  # Extract another skill
            "aboutstartapp": request.POST.get("aboutstartapp"),  # Extract about startapp
            "aboutteam": request.POST.get("aboutteam"),
            "skills2": request.POST.getlist("skills2"),
            "mvp": request.POST.get("mvp"),
            "startappimg": request.FILES.get("startappimg"),
            "startapppdf": request.FILES.get("startapppdf"),
        }

       
        print("Data received from POST request:", data)

        try:
            registration = models.Registration(
                full_name=data["name"],
                gender=data["gender"],  
                date_birth=data["date"],
                address=data["address"],
                phone=data["phonenumber"],
                startap_name=data["startappname"],
                another_category=data["anotherskill"],  
                about_startapp=data["aboutstartapp"],  
                about_team=data["aboutteam"],
                project_prototype=data["mvp"],
                startap_image=data["startappimg"],
                presentation=data["startapppdf"],
                agree=agree
            )
            registration.save()

            registration.category.set(data["skills"])
            registration.purpose.set(data["skills2"])

            messages.success(request, 'Your message has been sent successfully!')
            return redirect("common:success")

        except Exception as e:
            print("Error occurred:", str(e))
            traceback.print_exc()
            messages.error(request, f'An error occurred: {str(e)}')  
            return redirect("common:error")






class CourseView(View):
    def get(self, request):
        main = models.MainPage.objects.all().order_by("-id")
        course = models.Course.objects.all()
        major = models.Course.objects.values_list('name', flat=True)
        footer = models.Footer.objects.all()

        context = {
            'courses':course,
            'major': major,
            'main':main,
            'footer':footer,
        }
        return render(request, 'detail-courses.html', context)
    

    def post(self, request):
        print("++++++++++++++GOOOD+++++++++++++++++++++++++++")
        data = {
            "name": request.POST.get("name"),
            "major": request.POST.get("major"),  
            "age": request.POST.get("age"),
            "phone_number": request.POST.get("phone_number"),
        }
        print("Data received from POST request:", data)

        try:
            major_instance = get_object_or_404(models.Course, name=data["major"])  
            registration = models.CourseContact(
                name=data["name"],
                major=major_instance,  
                age=data["age"],
                phone_number=data["phone_number"],
            )
            registration.save()

            messages.success(request, 'Your message has been sent successfully!')
            return redirect("common:success")

        except Exception as e:
            print("Error occurred:", str(e))
            traceback.print_exc()
            messages.error(request, f'An error occurred: {str(e)}')  
            return redirect("common:error")
    




class ServiceView(View):
    def get(self, request):
        main = models.MainPage.objects.all().order_by("-id")
        about = models.Service.objects.all()
        typeservice = models.ServiceType.objects.all()
        product = models.Product.objects.all()
        footer = models.Footer.objects.all()

        context = {
            'about':about,    
            'main':main,
            'typeservice':typeservice,
            'product':product,
            'footer':footer,
        }
        return render(request, 'detail-factory.html', context)
    def post(self, request):
        print("++++++++++++++GOOOD+++++++++++++++++++++++++++")
        data = {
            "name": request.POST.get("name"),
            "phone_number": request.POST.get("phone_number"),
        }
        print("Data received from POST request:", data)

        try:
            registration = models.SeriveContact(
                name=data["name"],
                phone_number=data["phone_number"],
            )
            registration.save()

            messages.success(request, 'Your message has been sent successfully!')
            return redirect("common:success")

        except Exception as e:
            print("Error occurred:", str(e))
            traceback.print_exc()
            messages.error(request, f'An error occurred: {str(e)}')  
            return redirect("common:error")
