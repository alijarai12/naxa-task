from django.db import models

class CustomProjectManager(models.Manager):
    def get_special_objects(self):
        return self.filter(status=True)


    # Using the custom manager
objects = CustomProjectManager()   

