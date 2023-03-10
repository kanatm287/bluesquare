# Generated by Django 4.0.5 on 2023-03-08 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tech_task', '0002_alter_clients_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('U', 'undecided')], max_length=1)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_id', models.IntegerField(unique=True)),
                ('insurance_type', models.CharField(choices=[('L', 'life-insurance'), ('M', 'medical-insurance'), ('A', 'auto-insurance')], max_length=1)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tech_task.client')),
            ],
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
        migrations.AddConstraint(
            model_name='client',
            constraint=models.CheckConstraint(check=models.Q(('gender__in', ['M', 'F', 'U'])), name='tech_task_client_genders_valid'),
        ),
        migrations.AddConstraint(
            model_name='insurance',
            constraint=models.CheckConstraint(check=models.Q(('insurance_type__in', ['L', 'M', 'A'])), name='tech_task_insurance_insurance_type_valid'),
        ),
    ]
