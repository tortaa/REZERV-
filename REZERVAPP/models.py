from django.db import models


class profile(models.Model):
    name = models.CharField(max_length=264, unique=True)
    Email = models.CharField(max_length=264, unique=True)
    requests = models.ForeignKey('Request',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name+" "+self.picture+" "+self.Email

class best(models.Model):
    #best is the favourits
    profile_id = models.ManyToManyField('profile')
    resturant_id = models.ForeignKey('Resturant', on_delete=models.CASCADE,null=True,blank=True)



class Resturant(models.Model):
    name = models.CharField(max_length=264, unique=True)
    traffic = models.IntegerField(null=True, blank=True, default=0)
    rate = models.FloatField(null=True, blank=True, default=0)
    requests=models.ManyToManyField('Request',null=True,blank=True)
    location = models.CharField(max_length=264, unique=True)

class Request(models.Model):
    rest_admin_id = models.AutoField(primary_key=True)
    #time = models.TimeField(default="", editable=False)
    no_of_people = models.IntegerField(null=True, blank=True, default=0)
    #date = models.DateField(default="", editable=False)
    ACCEPTED = 'AC'
    REJECTED = 'REJ'
    CANCELED = 'CANC'
    PENDING = 'PEND'
    REQUEST_TYPES_CHOICES = [
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'rejected'),
        (CANCELED, 'canceled'),
        (PENDING, 'pending'),
    ]
    RequestTypes = models.CharField(max_length=264,choices=REQUEST_TYPES_CHOICES,default=ACCEPTED)

    def is_upperclass(self):
        return self.RequestTypes in (self.ACCEPTED , self.REJECTED, self.CANCELED, self.PENDING)

class ResturantAdmin (models.Model):
    name = models.CharField(max_length=264, unique=True)
    resturantid= models.ForeignKey('Resturant', on_delete=models.CASCADE,null=True,blank=True)
    requests=models.ManyToManyField('Request')
    traffic=models.IntegerField(null=True, blank=True, default=0)
