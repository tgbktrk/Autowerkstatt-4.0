# Generated by Django 5.0.7 on 2024-08-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0002_fileuploadmodel_problem_alter_measurement_car_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='problems',
        ),
        migrations.AddField(
            model_name='measurement',
            name='txt_file',
            field=models.FileField(default='', upload_to='files'),
        ),
        migrations.DeleteModel(
            name='Problem',
        ),
    ]
