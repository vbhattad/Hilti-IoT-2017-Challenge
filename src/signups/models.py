from django.db import models

# Create your models here.
class SignUp(models.Model):
    fname = models.CharField(max_length=150, null=True, blank=False)
    lname = models.CharField(max_length=150, null=True, blank=False)
    email = models.EmailField()
    
class MQTTSimulatorTable(models.Model):
    timestampdb = models.DateTimeField(auto_now_add=True)
    hboxtypedb = models.CharField(max_length=100)
    temperaturedb = models.FloatField()
    mq2db = models.FloatField()
    mq3db = models.FloatField()
    mq4db = models.FloatField()
    mq5db = models.FloatField()
    mq6db = models.FloatField()
    mq7db = models.FloatField()
    sounddb = models.FloatField()
    humiditydb = models.FloatField()
