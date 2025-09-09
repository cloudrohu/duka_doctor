from django.db import models
from django.utils import timezone
# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=100, blank=True)              # text field
    description = models.CharField(max_length=300, blank=True)        # short description
    image = models.ImageField(upload_to='sliders/')                   # image upload

    def __str__(self):
        return self.title
    


class Usp(models.Model):
    title = models.CharField(max_length=100, blank=True)              # text field
    description = models.CharField(max_length=300, blank=True)  


    def __str__(self):
        return self.title
    

class EmergencySection(models.Model):
    title = models.CharField(max_length=100, blank=True)              # text field
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title
    



class About(models.Model):
    # home/models.py (About model)
    Image = models.ImageField(upload_to="about/", null=True, blank=True)
    video_url = models.URLField(blank=True, null=True)
    Title = models.CharField(max_length=1000,)
    description = models.TextField(max_length=1000,)
    Mission = models.CharField(max_length=1000,)
    Vission = models.CharField(max_length=1000,)
    Doctors = models.CharField(max_length=1000,blank=True, null=True)
    Research_labs = models.CharField(max_length=1000,blank=True, null=True)
    Awards = models.CharField(max_length=1000,blank=True, null=True)
    Departments = models.CharField(max_length=1000,blank=True, null=True)




    def __str__(self):
        return self.Title


class Why_Choose(models.Model):
    title = models.CharField(max_length=150, blank=True) 
    description = models.CharField(max_length=500, blank=True)  

    def __str__(self):
        return self.title
    



class Services(models.Model):
    title = models.CharField(max_length=150, blank=True) 
    description = models.CharField(max_length=500, blank=True)  

    def __str__(self):
        return self.title
    


class Departments(models.Model):
    image = models.ImageField(upload_to='departments/')
    title = models.CharField(max_length=150, blank=True) 
    description = models.CharField(max_length=500, blank=True)  

    def __str__(self):
        return self.title
       

class Doctor(models.Model):
    image = models.ImageField(upload_to='doctors/')
    title = models.CharField(max_length=150, blank=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name="doctor", null=True, blank=True )
    twitter = models.CharField(max_length=150, blank=True)
    facebook = models.CharField(max_length=150, blank=True)
    instagram = models.CharField(max_length=150, blank=True)
    linkedin = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title
    


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=150, blank=True)    



    def __str__(self):
        return self.title
    


class FAQ(models.Model):
    Question = models.CharField(max_length=100, blank=True)
    Answer = models.CharField(max_length=300, blank=True)


    def __str__(self):
        return self.Answer
    

class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    
    logo = models.ImageField(upload_to='logo/')
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    whatsapp = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    google_map = models.CharField(blank=True,max_length=1000)
    copy_right = models.CharField(blank=True,max_length=100)
    icon = models.ImageField(upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    date = models.DateTimeField()
    department = models.ForeignKey('Departments', on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')
    doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return f"{self.name} — {self.date.strftime('%Y-%m-%d %H:%M')}"    