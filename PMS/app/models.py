from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

 
    def __str__(self):
        return f'{self.user.first_name} Profile'

    
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField()
    completed_status = models.BooleanField(default=False)
    project_start_date = models.DateField(auto_now_add=True)
    project_end_date = models.DateField()


    
class Attachment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to="file")
    attachment_date = models.DateField(null=True, blank=True)



