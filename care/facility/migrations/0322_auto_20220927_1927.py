# Generated by Django 2.2.11 on 2022-09-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0321_merge_20220921_2255'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='consultationbed',
            constraint=models.UniqueConstraint(condition=models.Q(consultation__admitted=True), fields=('consultation', 'bed'), name='unique_patient_bed'),
        ),
        migrations.AddConstraint(
            model_name='patientconsultation',
            constraint=models.UniqueConstraint(condition=models.Q(admitted=True), fields=('patient', 'current_bed'), name='unique_patient_bed'),
        ),
    ]
