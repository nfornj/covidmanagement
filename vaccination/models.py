from django.db import models

# Create your models here.


class States(models.Model):

    state_name = models.CharField(max_length=1024) # social media user
    state_id = models.IntegerField() # district id

    def __str__(self):
        return self.state_name

class Districts(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    state_id = models.IntegerField() # district id

    def __str__(self):
        return self.district_name

class Andaman_and_nicobar_islands(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Andhra_Pradesh(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Arunachal_Pradesh(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name