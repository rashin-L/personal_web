# Generated by Django 4.2.2 on 2023-07-03 15:45

from django.db import migrations, models
import files


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_remove_service_slug_alter_service_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='main_img',
            field=models.ImageField(blank=True, null=True, upload_to=files.FileUpload.upload_to),
        ),
    ]
