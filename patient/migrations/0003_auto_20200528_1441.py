# Generated by Django 3.0.5 on 2020-05-28 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0002_auto_20200528_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='user',
            field=models.ForeignKey(limit_choices_to=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]