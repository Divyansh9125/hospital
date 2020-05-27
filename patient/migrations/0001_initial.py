# Generated by Django 3.0.5 on 2020-05-27 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.BigIntegerField(blank=True, null=True)),
                ('pat_id', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1, null=True)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Address', models.CharField(blank=True, max_length=250, null=True)),
                ('Blood Group', models.CharField(choices=[('A+', 'A+ type'), ('A-', 'A- Type'), ('B-', 'B- Type'), ('B+', 'B+ Type')], max_length=2, null=True)),
                ('Case Paper no.', models.IntegerField(null=True)),
                ('Profile Picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
