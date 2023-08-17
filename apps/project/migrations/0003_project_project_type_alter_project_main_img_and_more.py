# Generated by Django 4.2.2 on 2023-06-25 05:15

from django.db import migrations, models
import files


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_objective_outcomes_achieved_role_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='main_img',
            field=models.ImageField(blank=True, null=True, upload_to=files.FileUpload.upload_to),
        ),
        migrations.AlterField(
            model_name='project',
            name='main_video',
            field=models.ImageField(blank=True, null=True, upload_to=files.FileUpload.upload_to),
        ),
        migrations.AlterField(
            model_name='project_gallery',
            name='project_img',
            field=models.ImageField(blank=True, null=True, upload_to=files.FileUpload.upload_to),
        ),
    ]
