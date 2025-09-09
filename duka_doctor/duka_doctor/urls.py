
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .import settings
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('thank_appointment', views.APPOINTMENT_THANKYOU, name='thank_appointment'),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
