from django.urls import path
from django.contrib.auth import views as auth_views
from hsptlapp.views import Index,Login,logout,Register,otp,Contact,Delete_Appoint,View_Appointment,About,Admin_login,Home
from hsptlapp.views import Add_Appointment,Doctor_login,Patient_login,cardiologist,Dermotologist,Gnecologist,Neurologist,Allergist,Success
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
app_name='hsptlapp'
urlpatterns = [
    path('', Home,name='home'),
    path('index',Index,name='index'),
    path('login/',Login,name='login'),
    path('logout/',logout,name='logout'),
    path('reg/',Register,name='register'),
    path('otp/<str:otp>/<str:username>/<str:password>/<str:email>/',otp, name='otp'),
    path('con/',Contact,name='contact'),
    path('delete_apponit(?p<int:pid>)',Delete_Appoint,name='delete_appoint'),
    path('view_appoint/',View_Appointment,name='view_appoint'),
    path('add_appoint/',Add_Appointment,name='Add_Appointment'),
    path('doctor/',Doctor_login,name='doctor'),
    path('patient_login/',Patient_login,name='patient_login'),
    path('cardiologist/', cardiologist,name='cardiologist'),
    path('Dermotologist/', Dermotologist,name='Dermotologist'),
    path('Gnecologist/', Gnecologist,name='Gnecologist'),
    path('Neurologist/', Neurologist,name='Neurologist'),
    path('Allergist/', Allergist,name='Allergist'),
    path('about/', About,name='about'),
    path('adm_login/', Admin_login,name='adm_login'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
     path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), 
          name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('cardiologist/', cardiologist,name='cardiologist'),
    path('Dermotologist/', Dermotologist,name='Dermotologist'),
    path('Gnecologist/', Gnecologist,name='Gnecologist'),
    path('Neurologist/', Neurologist,name='Neurologist'),
    path('Allergist/', Allergist,name='Allergist'),
    path('success/', Success,name='success'),
    



    
]