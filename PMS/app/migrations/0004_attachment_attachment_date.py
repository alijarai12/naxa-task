# Generated by Django 4.2.7 on 2023-12-01 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='attachment_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
