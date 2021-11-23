from django.contrib import admin
from Interface.models import alumniData,branchData,courseData, gallery


class alumniDataAdmin(admin.ModelAdmin):
    list_display = (('Name', 'Email', 'Course','Branch','BatchYear'))
    list_filter = ('Course','Branch','BatchYear')
    search_fields = ['Name', 'Email__email', 'Course__name','Branch__name','BatchYear']







admin.site.register(alumniData, alumniDataAdmin)
admin.site.register(gallery)
admin.site.register(branchData)
admin.site.register(courseData)