from django.contrib import admin
from common import models



admin.site.register(models.MainPage)
admin.site.register(models.InnoX)
admin.site.register(models.AboutUs)

@admin.register(models.Mentors)
class MentorsAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("description", )
    search_fields = ("description", "date")

@admin.register(models.WhyTexnopark)
class WhyTexnoparkAdmin(admin.ModelAdmin):
    list_display = ("title", )


@admin.register(models.StudentProject)
class StudentProjectAdmin(admin.ModelAdmin):
    list_display = ("title", )
    search_fields = ("description", "title")


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question", )
    search_fields = ("question", "answer")


admin.site.register(models.SliderContent)

@admin.register(models.SliderCompany)
class SliderCompanyAdmin(admin.ModelAdmin):
    list_display = ("name", )


admin.site.register(models.Footer)
admin.site.register(models.Service)

admin.site.register(models.ServiceType)
admin.site.register(models.Product)


admin.site.register(models.Registration)
admin.site.register(models.StartAppCategory)
admin.site.register(models.Purposes)


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", )



@admin.register(models.CourseContact)
class CourseContactAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", "phone_number")


@admin.register(models.SeriveContact)
class ServiceContactAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", "phone_number")