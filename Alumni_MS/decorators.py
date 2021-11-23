from django.core.exceptions import PermissionDenied
from Interface.models import alumniData



def user_is_alumni(function):
    def wrap(request, *args, **kwargs):
        u = request.user.first_name
        v = request.user.last_name
        full_name = u + ' ' + v
        data = alumniData.objects.filter(Name='Noel Jolly')
        if full_name == data:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap