from django.contrib import admin
from .models import Resume
# Register your models here.
class resume_data(admin.ModelAdmin):
    display = ['id', 'fullname', 'dob','gander','location','city','pin','state','mobile','email','job_city','profile','myfile']
admin.site.register(Resume, resume_data)