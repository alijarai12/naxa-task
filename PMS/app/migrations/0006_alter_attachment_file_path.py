# Generated by Django 4.2.7 on 2023-12-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_attachment_attachment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file_path',
            field=models.FileField(upload_to='file'),
        ),
    ]