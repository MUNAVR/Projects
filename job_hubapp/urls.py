from django.urls import path
from .import views

urlpatterns= [

   path('',views.index,name="home"),
   path('home' ,views.home),
   # user
   
   path('usignup',views.signup,name="usignup"),
   path('usignin',views.signin,name="usignin"),
   path('unav',views.unav,name="usernav"),
   path('jobdetails',views.details,name="details"),
   path('homejobs',views.homejobs),
   path('forget',views.forget),

   
   path('signin',views.usersignin,name="login"),
   path('signup',views.usersignup,name="signup"),
   path('logout',views.logout_view),
   path('fu',views.frpass),
   path('unav',views.unav,name="usernav"),
   path('jobsall',views.all_job,name="alljobs"),
   path("details/<int:id>/",views.job_details,name="jb"),
   path("apply/<int:id>/",views.job_apply,name="apply"),
   path('apply/<int:id>/applyjob',views.apply,name="submit"),
   path('myapply',views.myapp,name="my"),
   path('profile',views.pro,name="profile"),
   path('search',views.search),
  





# company

   path('signc',views.signupc,name="csignup"),
   path('csignin',views.signinc,name="csignin"),
   path('cmnyhm',views.chm,name="cmpnyhm"),
   path('cnav',views.cvan,name="compynav"),
   path('addjob',views.addjob,name="addjob"),
   path('listjob',views.lisjob,name="job"),
   path('editjob',views.editjob,name="editjob"),
   path('cprofile',views.cpro,name="profile"),
   path('cfr',views.cfr),


   path('csignup',views.companysignup,name="signc"),
   path('clo',views.companysignin,name="loginc"),
   path('logoutc',views.logout_views),
   path('cadd',views.addjob,name="addjob"),
   path('joblist',views.display,name="joblist"),
   path("update/<int:id>/",views.update,name="edit"),
   path('delete/<int:id>/',views.delete),
   path('allapplicant',views.all_applicant,name="allapplicant"),
   path('deleteap/<int:id>/',views.deleteap),
   path('candidates',views.candi),


   
   
]
