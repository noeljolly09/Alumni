from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from Interface.models import alumniData 

def login(request):
    if request.method=='POST':
        u1 = request.POST['uname']
        u2 = request.POST['psw']

        user = auth.authenticate(username=u1,password=u2)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Login unsuccesfull')  
            return redirect('login')
    else:
        return render(request, 'registration/login.html')


def register(request):

    if request.method == 'POST':
        user_name = request.POST['uname']
        user_email = request.POST['email']
        user_first_name = request.POST['f_name']
        user_last_name = request.POST['l_name']
        user_p1 = request.POST['psw']
        user_p2 = request.POST['cpsw']

        # w = user_first_name + " " + user_last_name
        # v = request.user.id

        if user_p1==user_p2:
            if User.objects.filter(username=user_name).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(username=user_name).exists():
                messages.error(request, 'Email already exists')
            else:
                
                user = User.objects.create_user(username=user_name,first_name=user_first_name,last_name=user_last_name,email=user_email,password=user_p1)
                user.save()
                # alumniData(Name = w,Email = user).save()

                return redirect('login')
        else:
            messages.error(request,'Passwords are not identical')
            return redirect('register')
    else:
        return render(request, 'registration/register.html')

  
def logout(request):
    auth.logout(request)
    return redirect('/')
