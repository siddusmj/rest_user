from django.db import models

# Create your models here.
from datetime import datetime
from timezone_utils.fields import LinkedTZDateTimeField, TimeZoneField
from timezone_utils.choices import PRETTY_ALL_TIMEZONES_CHOICES
# Create your models here.



class Names(models.Model):
    id = models.CharField(max_length=225, primary_key=True)
    real_name = models.CharField(max_length=250)
    timezone = TimeZoneField(choices=PRETTY_ALL_TIMEZONES_CHOICES)
    activity_periods = models.ManyToManyField('Periods')

    def __str__(self):
        return f'{self.id} {self.real_name} {self.timezone} '
 

  

def get_activity_periods_timezone(obj):
    return obj.activity_periods.timezone


   

     
class Periods(models.Model):
    start = LinkedTZDateTimeField(
    
        time_override=datetime.min.time()
    )
    end = LinkedTZDateTimeField(
      
        time_override=datetime.max.time()
    )


    def __str__(self):
        return f'{self.start} {self.end}'
