from django.db.models.query import RawQuerySet
from django.shortcuts import render,redirect
from . models import *
from Interface.models import alumniData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def jobsHome(request):
    user1 = request.user
    jobs = Job.objects.all()[:3]
    if Company.objects.filter(user=user1).exists():
        return redirect('recruiter_profile')
    elif Applicant.objects.filter(user=user1).exists():
        return redirect('applicant_profile')
    else:
        return render(request, "jobs/jobs_home.html", {'jobs':jobs})

@login_required
def applicantSignup(request):
    if request.method == 'POST':
        user1 = request.user
        phone = request.POST['phone']
        gender = request.POST['gender']
        image = request.FILES['image']
        applicants = Applicant.objects.create(user=user1, phone=phone, gender=gender, image=image, type="applicant")
        applicants.save()
        return redirect('applicant_profile')
    return render(request, 'jobs/applicant_signup.html')

@login_required
def applicantProfile(request):
    applicant = Applicant.objects.get(user=request.user)

    context = { 
        'applicant': applicant
    }
    return render(request, 'jobs/applicant_profile.html', context )

@login_required
def applicantUpdateProfile(request):
    applicant = Applicant.objects.get(user=request.user)
    if request.method == "POST":   
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone = request.POST['phone']
        gender = request.POST['gender']

        applicant.user.email = email
        applicant.user.first_name = first_name
        applicant.user.last_name = last_name
        applicant.phone = phone
        applicant.gender = gender
        applicant.save()
        applicant.user.save()

        try:
            image = request.FILES['image']
            applicant.image = image
            applicant.save()
        except:
            pass
        alert = True
        return render(request, "jobs/applicant_update_profile.html", {'alert':alert})
    return render(request, "jobs/applicant_update_profile.html", {'applicant':applicant})

@login_required
def availableJobs(request):
    jobs = Job.objects.all().order_by('-start_date')
    applicant = Applicant.objects.get(user=request.user)
    apply_for = Application.objects.filter(applicant=applicant)
    info = []
    for i in apply_for:
        info.append(i.job.id)
    context = {
        'jobs':jobs,
        'data':info,
    }
    return render(request,'jobs/applicant_jobs_available.html', context)

@login_required
def availableJobDetail(request, pk):
    job = Job.objects.get(id=pk)

    return render(request, 'jobs/applicant_available_job_detail.html',{'jobs':job})

@login_required
def availableJobApply(request, pk):
    applicant = Applicant.objects.get(user=request.user)
    job = Job.objects.get(id=pk)
    today_date = date.today()

    if job.end_date < today_date:
        closed = True
        return render(request, 'jobs/applicant_available_job_apply.html',{'closed':closed})
    elif job.start_date > today_date:
        notopen = True
        return render(request, 'jobs/applicant_available_job_apply.html',{'notopen':notopen})
    else:
        if request.method == 'POST':
            resume = request.FILES['resume']
            Application.objects.create(job=job, company=job.company, applicant=applicant, resume=resume, apply_date=date.today())
            alert =True
            return render(request, 'jobs/applicant_available_job_apply.html',{'alert':alert})
    return render(request,'jobs/applicant_available_job_apply.html',{'job':job})





@login_required
def recuriterSignup(request):

    user = User.objects.all()

    if request.method == 'POST':
        user1 = request.POST['username']
        phone = request.POST['phone']
        gender = request.POST['gender']
        image = request.FILES['company_logo']
        company_name = request.POST['company_name']

        if user1 == user.username:
            company = Company.objects.create(user=user1, phone=phone, gender=gender, image=image, company_name=company_name, type="company", status="pending")
            company.save()
            return redirect('recruiter_profile')
    return render(request, 'jobs/recruiter_signup.html')

@login_required
def recruiterProfile(request):
    recruiter = Company.objects.get(user=request.user)

    context = { 
        'recruiter': recruiter
    }
    return render(request, 'jobs/recruiter_profile.html', context )

@login_required
def recruiterUpdateProfile(request):
    recruiter = Company.objects.get(user=request.user)
    if request.method == 'POST':
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone = request.POST['phone']
        gender = request.POST['gender']

        recruiter.user.email = email
        recruiter.user.first_name = first_name
        recruiter.user.last_name = last_name
        recruiter.phone = phone
        recruiter.gender = gender
        recruiter.save()
        recruiter.user.save()

        try:
            image = request.FILES['image']
            recruiter.image = image
            recruiter.save()
        except:
            pass
        alert = True
        return render(request, "jobs/recruiter_update_profile.html", {'alert':alert})
    return render(request, "jobs/recruiter_update_profile.html", {'recruiter':recruiter})

@login_required
def recruiterAddJob(request):
    if request.method == "POST":
        title = request.POST['job_title']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        salary = request.POST['salary']
        experience = request.POST['experience']
        location = request.POST['location']
        skills = request.POST['skills']
        description = request.POST['description']
        user = request.user
        company = Company.objects.get(user=user)
        job = Job.objects.create(company=company, title=title,start_date=start_date, end_date=end_date, salary=salary, experience=experience, location=location, skills=skills, description=description, creation_date=date.today())
        job.save()
        alert = True
        return render(request, "jobs/recruiter_job_add.html", {'alert':alert})
    return render(request, "jobs/recruiter_job_add.html")

@login_required
def recruiterJobs(request):
    company1 = Company.objects.get(user=request.user)
    jobs = Job.objects.filter(company=company1)
    return render(request, 'jobs/recruiter_jobs_list.html', {'jobs':jobs})

@login_required
def recruiterJobUpdate(request, pk):
    job = Job.objects.get(id=pk)
    if request.method == "POST":
        title = request.POST['job_title']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        salary = request.POST['salary']
        experience = request.POST['experience']
        location = request.POST['location']
        skills = request.POST['skills']
        description = request.POST['description']

        job.title = title
        job.salary = salary
        job.experience = experience
        job.location = location
        job.skills = skills
        job.description = description

        job.save()
        if start_date:
            job.start_date = start_date
            job.save()
        if end_date:
            job.end_date = end_date
            job.save()
        alert = True
        return render(request, "jobs/recruiter_job_update.html", {'alert':alert})
    return render(request, "jobs/recruiter_job_update.html", {'job':job})

@login_required
def appliedApplicants(request):
    recruiter = Company.objects.get(user=request.user)
    application = Application.objects.filter(company=recruiter)
    return render(request, 'jobs/recruiter_applied_applicants.html',{'application':application})