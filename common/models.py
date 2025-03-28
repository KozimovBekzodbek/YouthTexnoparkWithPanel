from django.db import models
from django.core.validators import FileExtensionValidator, RegexValidator
from django.core.exceptions import ValidationError
from django_resized import ResizedImageField


class MainPage(models.Model):
    icon = models.FileField()
    title = models.CharField(max_length=256)
    main_img = ResizedImageField(size=[988, 800], quality=95,  crop=['middle', 'center'],   upload_to="main/%Y/%m")


    def __str__(self):
       return f"{self.title}"

    class Meta:

       db_table = "Asosiy"
       verbose_name = "Asosiy"
       verbose_name_plural = "Asosiy"



class InnoX(models.Model):
   name = models.CharField(max_length=256)
   image = ResizedImageField(size=[700, 473], quality=95,  crop=['middle', 'center'],   upload_to="main/%Y/%m")
   description = models.TextField()
   duration = models.CharField(max_length=256)
   lesson_duration = models.CharField(max_length=256)
   lesson_days = models.CharField(max_length=256)
   age_limit = models.CharField(max_length=256)
   requirements = models.TextField()

   def __str__(self):
      return f"{self.name}"
   
   class Meta:
      db_table = "Innox"
      verbose_name = "Innox"
      verbose_name_plural = "Innox"




class AboutUs(models.Model):
   description = models.TextField()
   image = ResizedImageField(size=[700, 473], quality=95,  crop=['middle', 'center'],   upload_to="main/%Y/%m")

   def __str__(self):
      return "AboutUs"
   
   class Meta:
      db_table = "AboutUs"
      verbose_name = "AboutUs"
      verbose_name_plural = "AboutUs"



class Mentors(models.Model):
   name = models.CharField(max_length=256)
   major = models.CharField(max_length=256)
   image = ResizedImageField(size=[405 , 500], quality=95,  crop=['middle', 'center'],   upload_to="mentors/%Y/%m")
   about = models.TextField()
   facebook = models.CharField(max_length=256)
   instagram = models.CharField(max_length=256)
   telegram = models.CharField(max_length=256)
   github = models.CharField(max_length=256)


   def __str__(self):
      return f"{self.name}"
   
   class Meta:
      db_table = "Mentors"
      verbose_name = "Mentors"
      verbose_name_plural = "Mentors"


class News(models.Model):
   date = models.CharField(max_length=256)
   image = ResizedImageField(size=[550,300],quality=95,  crop=['middle', 'center'],   upload_to="news/%Y/%m")
   description = models.TextField()

   def __str__(self):
      return f"{self.description}"
   
   class Meta:
      db_table = "News"
      verbose_name = "News"
      verbose_name_plural = "News"



class WhyTexnopark(models.Model):
   icon = ResizedImageField(quality=95, upload_to="main/%Y/%m")
   title = models.CharField(max_length=256)
   description = models.TextField()

   def __str__(self):
      return f"{self.title}"
   
   class Meta:
      db_table = "WhyTexnopark"
      verbose_name = "WhyTexnopark"
      verbose_name_plural = "WhyTexnopark"



class StudentProject(models.Model):
   title = models.CharField(max_length=256)
   image = ResizedImageField(size=[446,380], quality=95,  crop=['middle', 'center'],   upload_to="StudentProject/%Y/%m")
   description = models.TextField()

   def __str__(self):
      return f"{self.title}"
   
   class Meta:
      db_table = "StudentProject"
      verbose_name = "StudentProject"
      verbose_name_plural = "StudentProject"


   
class Question(models.Model):
   question = models.TextField()
   answer = models.TextField()
   is_top = models.BooleanField(default=False)


   def __str__(self):
      return self.question
   
   class Meta:
      db_table = "Questions"
      verbose_name = "Questions"
      verbose_name_plural = "Questions"


class SliderContent(models.Model):
   big_image = ResizedImageField(size=[550,650], quality=95,  crop=['middle', 'center'],   upload_to="SliderContent/%Y/%m")
   small_top_image = ResizedImageField(size=[550,315], quality=95,  crop=['middle', 'center'],   upload_to="SliderContent/%Y/%m")
   small_bottom_image = ResizedImageField(size=[550,315], quality=95,  crop=['middle', 'center'],   upload_to="SliderContent/%Y/%m")

   def __str__(self):
      return "Slider images"
   
   class Meta:
      db_table = "SliderContent"
      verbose_name = "SliderContent"
      verbose_name_plural = "SliderContent"



class SliderCompany(models.Model):
      image = models.FileField()
      name = models.CharField(max_length=256, null=True)

      def __str__(self):
          return "Slider companies"
   
      class Meta:
         db_table = "SliderCompany"
         verbose_name = "SliderCompany"
         verbose_name_plural = "SliderCompany"


class Footer(models.Model):
    icon = models.FileField()
    address = models.TextField()
    facebook = models.CharField(max_length=256)
    instagram = models.CharField(max_length=256)
    telegram = models.CharField(max_length=256)
    mail = models.CharField(max_length=256)

    def __str__(self):
          return "Footer"
   
    class Meta:
         db_table = "Footer"
         verbose_name = "Footer"
         verbose_name_plural = "Footer"
     



class Gender(models.TextChoices):
    Male = "Erkak", ("Erkak")
    FeMale = "Ayol", ("Ayol")


class YesNo(models.TextChoices):
    Yes = "Yes", ("yes")
    No = "No", ("no")
   
class StartAppCategory(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "startappcategory"
        verbose_name = "startappcategory"
        verbose_name_plural = "startappcategories"
        
    

class Purposes(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "purpose"
        verbose_name = "purpose"
        verbose_name_plural = "purpose"
    




class Registration(models.Model):
   full_name = models.CharField(max_length=256)
   gender = models.CharField(max_length=256,choices=Gender.choices)
   date_birth = models.DateField(null=True, blank=True)
   address = models.CharField(max_length=256)
   phone = models.CharField(max_length=256)
   startap_name = models.CharField(max_length=256)
   category = models.ManyToManyField(StartAppCategory)
   another_category=models.CharField(max_length=256, null=True)
   about_startapp = models.CharField(max_length=256) 
   about_team = models.CharField(max_length=256)
   purpose = models.ManyToManyField(Purposes)
   project_prototype = models.CharField(max_length=256,choices=YesNo.choices)
   startap_image = models.FileField(upload_to= "startap_image/%Y/%m")
   presentation = models.FileField(
        ("presentation"),
        validators=[FileExtensionValidator(["pptx", "pdf"])],
        upload_to= "presentation/%Y/%m"
    )
   agree = models.BooleanField(default=False)
   # status = models.BooleanField(default=False, null=True)  # New field to track status
   # timestamp = models.DateTimeField(auto_now_add=True, null=True) 

   def __str__(self):
       return f"{self.full_name}"

   class Meta:
       db_table = "form"
       verbose_name = "form"
       verbose_name_plural = "forms"


class Course(models.Model):
   name = models.CharField(max_length=256)
   about = models.TextField()
   duration = models.CharField(max_length=256)
   lesson_duration = models.CharField(max_length=256)
   lesson_days = models.CharField(max_length=256)
   age_limit = models.CharField(max_length=256)
   image = ResizedImageField(size=[600, 600], quality = 95, crop=['middle', 'center'], upload_to='courses/%Y/%m')
   

   def __str__(self):
       return f"{self.name}"

   class Meta:
       db_table = "course"
       verbose_name = "course"
       verbose_name_plural = "courses"



class CourseContact(models.Model):
   name = models.CharField(max_length=256)
   major = models.ForeignKey(Course, on_delete=models.CASCADE)
   age = models.CharField(max_length=2)
   phone_number = models.CharField(max_length=13)


   def __str__(self):
       return f"{self.name}"

   class Meta:
       db_table = "CourseContact"
       verbose_name = "CourseContact"
       verbose_name_plural = "CourseContacts"
   



class Service(models.Model):
   title = models.CharField(max_length=256)
   about = models.TextField()
   image = ResizedImageField(size=[456,474], quality = 95, crop=['middle', 'center'], upload_to='services/%Y/%m')
    
    

   def __str__(self):
        return f"{self.title}"

   class Meta:
       db_table = "Service"
       verbose_name = "Service"
       verbose_name_plural = "Services"


class ServiceType(models.Model):
    icon = models.FileField()
    title = models.CharField(max_length=256)
    about = models.TextField()


    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        db_table = "ServiceType"
        verbose_name = "ServiceType"
        verbose_name_plural = "ServiceType"


class Product(models.Model):
   title = models.CharField(max_length=256)
   about = models.TextField()
   image = ResizedImageField(size=[330,530], quality = 95, crop=['middle', 'center'], upload_to='serviceproduct/%Y/%m')


   def __str__(self):
       return f"{self.title}"
   

   class Meta:
       db_table = "Product"
       verbose_name = "Product"
       verbose_name_plural = "Products"
    

class SeriveContact(models.Model):
   name = models.CharField(max_length=256)
   phone_number = models.CharField(max_length=13)


   def __str__(self):
       return f"{self.name}"

   class Meta:
       db_table = "SeriveContact"
       verbose_name = "SeriveContact"
       verbose_name_plural = "SeriveContacts"