from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from.models import Applicants,Company,Job,Application
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required,permission_required
from datetime import date
from .forms import MyFileForm
from django.urls import path

from io import BytesIO
from django.template.loader import get_template
from django.views import View
from job_hub import settings
import os
from django.core.files.storage import FileSystemStorage
# from xhtml2pdf import pisa




uploaded_file_url=""

# Create your views here.
def index(request):
    return render(request,"home.html")

def home (request):
    return render (request , "home.html")



#user


def signup(request):
    return render(request,"signup_user.html")

def signin(request):
    return render(request,"user_login.html")

def logout_view(request):
    logout(request)
    return redirect('usignin')

def forget(request):
    return render(request,"fogetuser.html")

def reset(request):
    return render(request,"resetpassword.html")

def uhome(request):
    return render(request,"userhome.html")

def unav(request):
    return render(request,"usernav.html")

def all(request):
    return render(request,"alljobs.html")

def details(request):
    return render(request,"job_details.html")

def myapply(request):
    return render(request,"myapplication.html")

def pro (request):
    return render(request,"profile.html")

def usersignup(request):
    if request.method == "POST":
        user_name=request.POST['uname']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        password=request.POST['password']
        phone_number=request.POST['number']
        gender =request.POST['gender']
        email =request.POST['mail']
        resume =request.POST['resume']
        profile =request.POST['photo']
        
        user=User.objects.create_user(username=user_name,password=password)
        Applicant =Applicants(firstname=first_name,lastname=last_name,username=user,email=email,phone=phone_number,
                              gender=gender,profile=profile,resume=resume)
        user.save()
        group = Group.objects.get(name="Applicant")
        user.groups.add(group)
        Applicant.save()
        return redirect('usernav')
    else:
        return render(request,"signup_user.html")
 
def usersignin(request):
    username=request.POST['name']
    pwd=request.POST['password']
    user=authenticate(request,username=username,password=pwd)
    if user is not None:
        login(request,user)
        userGroup = Group.objects.get(user=request.user).name
        if userGroup =='Applicant':
            return redirect('usernav')
        else:
            return render (request,"user_login.html",{'msg': 'Invalid Login'})
        
    else:
        return render(request,"user_login.html", {'msg': 'Invalid Login'})
    

def frpass(request):
    responseDic={}
    username=request.POST['name']
    email=request.POST['email']
    mobile=request.POST['mbl']
    newpass=request.POST['password']

    try:
        user=User.objects.get(username=username)
        em=Applicants.objects.get(email=email)
        mbl=Applicants.objects.get(phone=mobile)
        if user is not None :
            user.set_password(newpass)
            user.save()
            responseDic["errmsg"]="password Reset Successfully"
            return redirect('usignin')
    except Exception as e:
        print(e)
        responseDic["errmsg"] = "Password Request Failed"
        return render (request,"fogetuser.html",responseDic)



    
def all_job(request):
    jobs=Job.objects.all()
    content = { 
        'jobs':jobs,
    }
    return render (request,"alljobs.html",content)

def job_details(request,id):
    jobs=Job.objects.get(id=id)
    return render (request,"Job_details.html",{'jobs':jobs})

def job_apply(request,id):
    return render(request,"job_apply.html")

def apply(request,id):
    global uploaded_file_url
    applicant=Applicants.objects.get(username=request.user)
    job= Job.objects.get(id=id)
    company=Company.objects.get(company_name=job.company)
    date1=date.today()
    # if job.end_date < date1:
    #     closed=True
    #     return render(request,"job_apply.html",{'msg1':job is closed})
    # elif job.start_date > date1:
    #     noteopen=True  
    #     return render(request,"job_apply.html",{'msg2':job is not open})
    # else:
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        cd=Application.objects.create(job=job,company=company,applicant=applicant,resume=myfile,apply_date=date.today())
        cd.save()
        return redirect('alljobs')
    else:
         return render(request,"job_apply.html")

def myapp (request):
    applicant=Applicants.objects.get(username=request.user)
#job= Job.objects.filter(id=
    applications=Application.objects.filter(applicant=applicant)
    content = { 
        'jobs':applications,
    }
    return render (request,"myapplication.html",content)

def homejobs(request):
    jobs=Job.objects.all()
    content = { 
        'jobs':jobs,
    }
    return render (request,"homejobs.html",content)

def pro(request):
    app=Applicants.objects.get(username=request.user)
    context ={
        'app' : app,
    }
    return render (request,"profile.html",context)

def search (request) :
    typejob=request.POST['search']
    job= Job.objects.filter(title=typejob)
    content={
        'se':job
    }
    return render (request,"alljobs.html",content )








# Company

def signupc(request):
    return render(request,"company_signup.html")

def signinc(request):
    return render(request,"signin_company.html")

def cfr(request):
    return render (request,"forgetcompany.html")

def chm(request):
    return render(request,"addjob.html")
#@permission_required  
def cvan(request):
    return render(request,"companynav.html")

def addjob(request):
    return render(request,"addjob.html")

def editjob(request):
    return render(request,"edit_job.html")

def lisjob(request):
    return render(request,"job_list.html")

def cpro(request):
    return render(request,"cprofile.html")

def candi(request):
    return  render (request,"candidates.html")


def companysignup(request):
    if request.method =="POST":
        username=request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['number']
        company_name=request.POST['company_name']
        logo=request.POST['photo']
        type=request.POST['type']
        location=request.POST['location']
        address=request.POST['address']


        company=User.objects.create_user(username=username,password=password)
        cmpy=Company(username=company,email=email,phone=phone,company_name=company_name,
                     address=address,logo=logo,type=type,location=location)
        company.save()
        cmpy.save()
        return redirect('compynav')
    else:
        return render(request,"signin_company.html")


def companysignin(request):
    username=request.POST['name']
    pwd=request.POST['password']
    user=User.objects.filter(groups__name='company')
    company=authenticate(request,username=username,password=pwd)
    if company is not None :
        login(request,company)
        userGroup = Group.objects.get(user=request.user).name
        if userGroup == 'company':
            return redirect('compynav')
        else:
             return render(request,"signin_company.html", {'msg': 'Invalid Login'}) 
    else:
        return render(request,"signin_company.html", {'msg': 'Invalid Login'})
    

def logout_views(request):
    logout(request)
    return redirect('csignin')
    
def frpass(request):
    responseDic={}
    username=request.POST['name']
    email=request.POST['email']
    mobile=request.POST['mbl']
    newpass=request.POST['password']

    try:
        user=User.objects.get(username=username)
        em=Applicants.objects.get(email=email)
        mbl=Applicants.objects.get(phone=mobile)
        if user is not None :
            user.set_password(newpass)
            user.save()
            responseDic["errmsg"]="password Reset Successfully"
            return redirect('csignin')
    except Exception as e:
        print(e)
        responseDic["errmsg"] = "Password Request Failed"
        return render (request,"fogetuser.html",responseDic)
    

def addjob(request):
    if request.method =="POST":
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        title=request.POST['job_title']
        salary=request.POST['salary']
        description=request.POST['description']
        experience=request.POST['exp']
        location=request.POST['Location']
        skills=request.POST['skills']
        vacancy=request.POST['vacancy']
        qualification=request.POST['qualification']
        
        
        user=request.user
        company=Company.objects.get(username=user)
        job =Job(company=company,start_date=start_date,end_date=end_date,title=title,salary=salary,description= description,
                 experience=experience,location=location,skills=skills,vacancy=vacancy, qualification=qualification,creation_date=date.today())
        job.save()
        return redirect('compynav')
    else:
        return render (request,"addjob.html")


def display(request):
    companies=Company.objects.get(username=request.user)
    jobs=Job.objects.filter(company=companies)
    content = { 
        'jobs':jobs,
    }
    return render (request,"job_list.html",content)
    

def update(request,id):
    edit=Job.objects.get(id=id)

    title=edit.title
    salary=edit.salary
    description=edit.description
    experience=edit.experience
    location=edit.location
    skills=edit.skills
    vacancy=edit.vacancy
    qualification=edit.qualification
    start_date=edit.start_date
    end_date=edit.end_date
        
    if request.method =="POST":   
        if title:
            edit.title = request.POST['job_title']
            edit.save()
        if salary:
            edit.salary = request.POST['salary']
            edit.save()
        if description:
            edit.description=request.POST['description']
            edit.save()
        if experience:
            edit.experience=request.POST['exp']
            edit.save()
        if location:
            edit.location=request.POST['Location']
            edit.save()
        if skills:
            edit.skills=request.POST['skills']
            edit.save()
        if vacancy:
            edit.vacancy=request.POST['vacancy']
            edit.save()
        if qualification:
            edit.qualification=request.POST['qualification']
            edit.save()
        if start_date:
            edit.start_date=request.POST['start_date']
            edit.save()
        if end_date:
            edit.end_date=request.POST['end_date']
            edit.save()
        return redirect('joblist')
    return render(request,"edit_job.html",{'edit':edit})


def delete(request,id):
    jobs=Job.objects.get(id=id)
    jobs.delete()
    return redirect('joblist')

def all_applicant(request):
    global uploaded_file_url
    company=Company.objects.get(username=request.user)
    mydata=Application.objects.filter(company=company)
    # myform=MyFileForm(request.POST,request.FILES)
    # myfile = request.FILES['myfile']
    # fs = FileSystemStorage()
    # filename = fs.save(myfile.name, myfile)
    # uploaded_file_url = fs.url(filename)
    
    #if request.method == 'POST' and request.FILES['myfile']:
    #   myfile = request.FILES['myfile']
    #uploaded_file_url = fs.url(mydata.resume.path)
    return render(request, "all_applicant.html", {
        'uploaded_file_url':uploaded_file_url,"mydata":mydata
        })

def deleteap(request,id):
    appliction=Application.objects.get(id=id)
    appliction.delete()
    return redirect('allapplicant')


def cpro(request):
    app=Company.objects.get(username=request.user)
    context ={
        'app' : app,
    }
    return render (request,"cprofile.html",context)


