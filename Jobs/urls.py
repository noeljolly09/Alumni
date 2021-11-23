
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.jobsHome, name='jobs_homepage'),

    #applicant

    path('applicant/signup', views.applicantSignup, name='applicant_signup'),

    path('applicant/profile', views.applicantProfile, name='applicant_profile'),

    path('applicant/updateprofile', views.applicantUpdateProfile, name='applicant_update_profile'),

    path('applicant/available/jobs',views.availableJobs, name="applicant_available_jobs"),

    path('applicant/available/job/detail/<int:pk>',views.availableJobDetail,name="applicant_available_job_detail"),

    path('applicant/available/job/apply/<int:pk>',views.availableJobApply,name="applicant_available_job_apply"),





    #recruiter
    path('recruiter/signup', views.recuriterSignup, name='recruiter_signup'),

    path('recruiter/profile', views.recruiterProfile, name='recruiter_profile'),

    path('recruiter/updateprofile', views.recruiterUpdateProfile, name='recruiter_update_profile'),

    path('recruiter/job/add',views.recruiterAddJob, name='recruiter_job_add'),

    path('recruiter/job/list',views.recruiterJobs,name='recruiter_job_list'),

    path('recruiter/job/update/<int:pk>',views.recruiterJobUpdate,name='recruiter_job_update'),
    path('recruiter/job/applied/applicant',views.appliedApplicants,name='recruiter_applied_applicants'),
]

