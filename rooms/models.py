from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Room(models.Model):
    roomid=models.CharField(max_length=5)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.roomid

class Customer(models.Model):
    name=models.TextField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    room=models.ForeignKey(Room,on_delete=models.PROTECT)
    personalid=models.CharField(max_length=100)
    idnumber=models.CharField(max_length=16)
    checkedin=models.DateTimeField(auto_now_add=True)
    checkout=models.DateTimeField(blank=True,null=True)
    bill=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.name
