
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.views.static import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/',include('django.contrib.auth.urls')),
    path('', include('Interface.urls')),
    path('accounts/', include('accounts.urls')),
    path('blog/',include('Blog.urls')),
    path('jobs/', include('Jobs.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 