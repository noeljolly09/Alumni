from django.contrib import admin
from Interface.models import alumniData,branchData,courseData, gallery


class alumniDataAdmin(admin.ModelAdmin):
    list_display = (('Name','Designation', 'Email', 'Course','Branch','BatchYear'))
    list_filter = ('Course','Branch','BatchYear','Designation')
    search_fields = ['Name', 'Email__email', 'Course__name','Branch__name','BatchYear','Designation']







admin.site.register(alumniData, alumniDataAdmin)
admin.site.register(gallery)
admin.site.register(branchData)
admin.site.register(courseData)