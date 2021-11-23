from django.contrib import admin
from Jobs.models import *


# class alumniDataAdmin(admin.ModelAdmin):
#     list_display = (('Name', 'Email', 'Course','Branch','BatchYear'))
#     list_filter = ('Course','Branch','BatchYear')
#     search_fields = ['Name', 'Email__email', 'Course__name','Branch__name','BatchYear']







# admin.site.register(alumniData, alumniDataAdmin)
admin.site.register(Applicant)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Application)