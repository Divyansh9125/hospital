from django.shortcuts import render, redirect
from .forms import ProfileUpdateform
from django.contrib.auth.decorators import login_required
from .models import PatientProfile
from reception.models import Appointments

@login_required
def homeView(request):
    curr_user = request.user
    if curr_user.label == 'P':
        return render(request, 'patient/home.html')
    else:
        return redirect('login')
        

@login_required
def ProfileView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'P':
            if request.method == 'POST':
                form = ProfileUpdateform(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('pat-home')
                
            else:
                form = ProfileUpdateform()
                return render(request, 'patient/profile.html', {'form': form})
        else:
            return redirect('login')


@login_required
def AppointmentView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'P':
            pat = PatientProfile.objects.get(user=curr_user)
            all_apps = Appointments.objects.all().filter(pat=pat).order_by('time')
            return render(request, 'patient/appointments.html', {'allapp': all_apps})
        else:
            return redirect('login')
