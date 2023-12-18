from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
import random
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect

def Index(request):
    return render(request,'index.html')

def send_otp(email, otp):
    subject = 'OTP Verification'
    message = f'Your OTP for registration is: {otp}'
    send_mail(subject, message, None, [email])

def Register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('hsptlapp:register')

        otp_number = random.randint(1000, 9999)
        otp = str(otp_number)

        send_otp(email, otp)
        request.session['username'] = username
        request.session['email'] = email
        request.session['password'] = password
        request.session['otp'] = otp  # Add this line to store OTP in the session

        # Construct the URL using HttpResponseRedirect
        #return HttpResponseRedirect(f'/otp/{otp}/{username}/{password}/{email}/')
        # Alternatively, you can use reverse:
        return HttpResponseRedirect(reverse('hsptlapp:otp', args=[otp, username, password, email]))

    else:
        return render(request, 'register.html')

def otp(request, otp, username, password, email):
    if request.method == "POST":
        uotp = request.POST['otp']
        otp_from_session = request.session.get('otp')

        if uotp == otp_from_session:
            username = request.session.get('username')
            email = request.session.get('email')
            password = request.session.get('password')

            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.info(request,'Registerd sucessfully')
            return redirect('hsptlapp:login')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('hsptlapp:otp', otp=otp, username=username, password=password, email=email)

    return render(request, 'otp.html',{'otp': otp, 'username': username, 'password': password, 'email': email})

def Login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,'Logged in sucessfully')
            return redirect('hsptlapp:doctor')
        else:
            messages.info(request,'Invalid user credentials')
            return redirect('hsptlapp:login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout (request)
    return redirect('hsptlapp:index')

def Contact(request):
    return render(request,'contact.html')


def Doctor_login(request):
    return render(request,'doctor.html')

def Patient_login(request):
    return render(request,'patient login.html')

def Delete_Appoint(request,pid):
    appoint = Appointment.objects.get(id=pid)
    appoint.delete()
    return redirect('hsptlapp:view_appoint')

def Add_Appointment(request):
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor')
        patient_name = request.POST.get('patient')
        appointment_date = request.POST.get('Date')
        gender = request.POST.get('Gender')
        appointment_time = request.POST.get('Time')
        
        doctor = Doctor.objects.filter(name=doctor_name).first()
        
        if doctor:
            appointment = Appointment(
                name=doctor,
                patient_name=patient_name,
                gender=gender,
                date=appointment_date,
                time=appointment_time,
            )
            appointment.save()
            messages.success(request,'Appointment added successfully.')
            return redirect('hsptlapp:success')
        else:
            messages.error(request, 'Doctor not found.')
            return redirect('hsptlapp:Add_Appointment')

    context = {'doctor1': doctors}
    return render(request, 'add_appointment.html', context)

def View_Appointment(request):
    app = Appointment.objects.all()
    print(app)
    a = {'app':app}
    return render(request,'view_appointment.html',a)
  
def cardiologist(request):
    return render(request,'cardiologist.html')

def Dermotologist(request):
    return render(request,'Dermotologist.html')

def Gnecologist(request):
    return render(request,'Gnecologist.html')

def Neurologist(request):
    return render(request,'Neurologist.html')

def Allergist(request):
    return render(request,'Allergist.html')

def Success(request):
    return render(request,'success.html')

def About(request):
    return render(request,'About.html')
   
def Admin_login(request):
    return render(request,'admin_login.html')

def Home(request):
    return render(request,'home.html')
