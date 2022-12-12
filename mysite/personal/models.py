from django.db import models

# Create your models here.
class Shows(models.Model):
    # Default behaviour - Django creates primary keys for you
    date = models.DateField('show date')
    time = models.TimeField('show time')
    location = models.CharField(max_length=250, default = "")

    def __str__(self):
        return self.location
    
