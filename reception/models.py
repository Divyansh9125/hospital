from django.db import models
from doctor.models import DoctorProfile
from patient.models import PatientProfile

class Appointments(models.Model):
    Pending = 'PD'
    Completed = 'CT'
    statusChoice = [
        (Pending, 'Pending'),
        (Completed, 'Completed'),
    ]
    time = models.TimeField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=statusChoice)
    pat = models.ForeignKey(PatientProfile, on_delete=models.SET_DEFAULT, null=True, default=None)
    doc = models.ForeignKey(DoctorProfile, on_delete=models.SET_DEFAULT, null=True, default=None)

    class Meta:
        unique_together = ['time', 'date', 'pat', 'doc']
