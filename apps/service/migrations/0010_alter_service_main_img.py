# Generated by Django 4.1.4 on 2023-08-10 21:05

from django.db import migrations, models
import files


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_alter_service_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='main_img',
            field=models.ImageField(blank=True, null=True, upload_to=files.FileUpload.upload_to),
        ),
    ]
