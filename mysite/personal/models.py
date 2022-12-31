from django.db import models

# Create your models here.
class Shows(models.Model):
    '''
    This is the Model Database to store any data regarding any shows that the band has.
    This is then used on the site to display to the user all the data.

    :param Date: Shows the date the show is happening.
    :type Date: DateField

    :param Time: Shows the time the show is happening.
    :type Time: TimeField

    :param Location: Shows the location where the show is happening. 
    :type Location: CharField
    '''
    # Default behaviour - Django creates primary keys for you
    date = models.DateField('show date')
    time = models.TimeField('show time')
    location = models.CharField(max_length=250, default = "")

    def __str__(self):
        return self.location
    