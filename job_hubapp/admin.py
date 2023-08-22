from django.contrib import admin
from .models import Applicants,Company,Job,Application

# Register your models here.
class ApplicantsAdmin(admin.ModelAdmin):
    list_display = ('id','firstname','username')
    ordering = ('firstname',)
    search_fields=('firstname','username')
admin.site.register(Applicants,ApplicantsAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','company_name','username')
    ordering = ('company_name',)
    search_fields=('company_name','username')
admin.site.register(Company,CompanyAdmin)


class  JobAdmin(admin.ModelAdmin):
    list_display = ('id','title','company')
    ordering = ('title',)
    search_fields=('title','company')
admin.site.register(Job,JobAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id','job','company','applicant')
    ordering = ('job',)
    search_fields=('job','company','applicant')
admin.site.register(Application,ApplicationAdmin)