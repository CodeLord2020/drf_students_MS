# Generated by Django 4.1.7 on 2023-06-19 12:02

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
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('level', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='patient_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=100)),
                ('ailment', models.CharField(max_length=100)),
                ('residence', models.CharField(max_length=100)),
                ('next_of_kin', models.CharField(max_length=100)),
                ('Relation_with_NOK', models.CharField(max_length=100)),
                ('nok_contact', models.CharField(max_length=100)),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
        migrations.CreateModel(
            name='hostel_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_name', models.CharField(max_length=100)),
                ('location', models.CharField(choices=[('Obanla', 'Obanla'), ('Obakekere', 'Obakekere'), ('West-gate', 'West-gate')], max_length=20)),
                ('No_of_roommates', models.IntegerField(null=True)),
                ('block_and_room_number', models.CharField(max_length=100)),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]
