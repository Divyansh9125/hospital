from doctor.models import DoctorProfile
from patient.models import PatientProfile
from .models import Appointments
from django import forms

class AddAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['time', 'doc', 'pat', 'status']
        def __init__(self, *args, **kwargs):
            model = Appointments
            user = kwargs.pop('user','')
            super(AddAppointmentForm, self).__init__(*args, **kwargs)
            self.fields['doc']=forms.ModelChoiceField(queryset=DoctorProfile.objects.all())
            self.fields['pat']=forms.ModelChoiceField(queryset=PatientProfile.objects.all())

class GetPkIDForm(forms.Form):
    pk_id = forms.IntegerField()