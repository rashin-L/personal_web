# Generated by Django 4.1.4 on 2023-08-10 21:29

from django.db import migrations, models
import files


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_socialmedia_alter_introduction_cv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introduction',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to=files.FileUpload.upload_to),
        ),
        migrations.AlterField(
            model_name='introduction',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=files.FileUpload.upload_to),
        ),
        migrations.AlterField(
            model_name='introduction',
            name='main_img',
            field=models.ImageField(blank=True, null=True, upload_to=files.FileUpload.upload_to),
        ),
    ]
