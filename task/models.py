from django.db import models
from django.utils import timezone

# Create your models here.
class terms (models.Model):
    taskName = models.CharField(max_length=50, blank=True, default=None)

    def __str__(self):
        return (self.taskName)
    
class taskmaster(models.Model):
    date = models.DateField(default=timezone.now)
    task = models.ForeignKey(terms, on_delete=models.CASCADE)
    enquiryNo =  models.IntegerField()
    timetaken =  models.IntegerField()
    comments = models.TextField(blank=False, default=None)
    userid = models.TextField(blank=True)
    
    
    
    