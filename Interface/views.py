from django.contrib.auth import models
from django.http.response import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.models import AnonymousUser, User

from django.views.generic import CreateView, UpdateView, ListView
from django.views.generic import detail
from django.views.generic.detail import DetailView
from Alumni_MS.decorators import user_is_alumni

from Events.models import eventsData
from Blog.models import Post
from Interface.models import alumniData, gallery
from Jobs.models import Job



def home(request):
    
    home_blogs = Post.objects.all()[:3]
    home_images = gallery.objects.all()[:3]
    home_jobs = Job.objects.all()[:4]
    home_alumni = alumniData.objects.all()[:4]
    data = alumniData.objects.all().count()
    home_events = eventsData.objects.all()[:3]


    context = {
            'home_images':home_images,
            'home_blogs':home_blogs,
            'home_jobs':home_jobs,
            'data':data,
            'home_alumni':home_alumni,
            "home_events":home_events,
    }  
    return render(request, 'index.html',context)


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request,'contact.html')


# def nav(request):
#     alumni = alumniData.objects.filter(Email = request.user.email)
#     print(alumni)

#     if alumni.exists:
#         created = True
#         return render(request, 'nav.html',{'created':created})
#     return redirect('homepage')

''' Gallery part'''

class GalleryImages(ListView):
    model= gallery
    template_name = 'gallery/gallery_images.html'

class AddImagesGallery(CreateView):
    model = gallery
    template_name = 'gallery/add_images_gallery.html'
    fields = '__all__'


'''Alumni Directory Part'''


class Alumnidirectory(ListView):
    model = alumniData
    template_name = 'alumni/alumnidirectory.html'

class MyProfile(DetailView):
    model = alumniData
    template_name = 'alumni/alumni_detail.html'

class AddAlumni(CreateView):
    model = alumniData
    template_name = 'alumni/add_alumni.html'
    fields = '__all__'

class UpdateProfile(UpdateView):
    model = alumniData
    template_name = 'alumni/update_alumni.html'
    fields = '__all__'

    def get_success_url(self):
        view_name = 'alumniprofile'
        return reverse(view_name, kwargs={'pk': self.object.pk})


#user profile 

def Profile(request):
    
    if User.is_authenticated:
        u = request.user.first_name
        v = request.user.last_name
        full_name = u + ' ' + v
        data = alumniData.objects.filter(Name=full_name)
        context = {'data':data}
        return render(request, 'alumni/Myprofile.html', context)
