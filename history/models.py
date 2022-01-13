from pickle import STOP
from django.db import models
from django.contrib.auth.models import User


class LineHistory(models.Model):
    line = models.CharField(max_length=50)
    assembly = models.CharField(max_length=100)
    line_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Lines"
    
    def __str__(self):
        return self.line 

#carrier model
class Carrier_number(models.Model):
    GREASE_CHOICES = (('ultra', 'Ultra'), ('premier', 'Premier'))
     
    carrier_num = models.IntegerField()
    greasing = models.CharField(max_length=10, choices= GREASE_CHOICES, default= 'premier')

    def __str__(self):
        return str(self.carrier_num)

class Carrier(models.Model):

    carrier_num = models.ForeignKey(Carrier_number,default=1, on_delete=models.SET_DEFAULT)
    created = models.DateTimeField(auto_now_add=True)
    work_done = models.TextField(blank=True)
    changed_date = models.DateField()
    carrier_slug = models.SlugField(max_length=100, default=1 )
    front_pickup_trolly = models.DateField(null=True, blank=True)
    front_rear_trolly = models.DateField(null=True, blank=True)
    rear_pickup_trolly = models.DateField(null=True, blank=True)
    rear_nonpickup_trolly = models.DateField(null=True, blank=True)
    front_kingpin = models.DateField(null=True, blank=True)
    rear_kingpin = models.DateField(null=True, blank=True)
    def __str__(self):
        return str(self.carrier_num)

# stop model
class Stop_numbers(models.Model):
    STOP_TYPE =(('oven', 'Oven'),('lh', 'Lh'),('rh', 'Rh'))
    stop_number = models.IntegerField()
    stop_type = models.CharField(max_length= 10, choices = STOP_TYPE, default ='lh')
    def __str__(self):
        return str(self.stop_number)

class Stop(models.Model):
    stop = models.ForeignKey(Stop_numbers, default = 1, on_delete=models.SET_DEFAULT)
    changed_date = models.DateField()
    greasing_date = models.DateField()
    work_done = models.CharField(max_length=100, blank=False)
    work_done_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return str(self.stop)

#tsw model 
class Tsw_number(models.Model):
    TSW_TYPE = (('tsw', 'Tsw'), ('retrocate', 'Retrocate'))
    tsw_number = models.IntegerField()
    tsw_type = models.CharField(max_length = 15, choices = TSW_TYPE, default = 'Tsw')
    def __str__(self):
        return str(self.tsw_number )
    
class Tsw(models.Model):
    tsw = models.ForeignKey(Tsw_number, default=1, on_delete=models.SET_DEFAULT)
    bearing_change_date = models.DateField()
    work_done = models.CharField(max_length = 100, blank= False)
    work_done_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return str(self.tsw)
