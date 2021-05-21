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

class Assam(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Bihar(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Chandigarh(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Chhattisgarh(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Dadra_and_nagar_haveli(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Daman_and_diu(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Delhi(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Goa(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Gujarat(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Haryana(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Himachal_pradesh(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Jammu_and_kashmir(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Jharkhand(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Karnataka(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Kerala(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Ladakh(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Lakshadweep(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Madhya_pradesh(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Maharashtra(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Manipur(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Meghalaya(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Mizoram(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Nagaland(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Odisha(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Puducherry(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Punjab(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Rajasthan(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Sikkim(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Tamil_nadu(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Telangana(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name


class Tripura(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Uttar_pradesh(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class Uttarakhand(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name

class West_bengal(models.Model):

    district_name = models.CharField(max_length=1024) # social media user
    district_id = models.IntegerField() # district id
    name = models.CharField(max_length=1024) # hospital_name
    vaccine_date = models.DateField() #date created
    available_capacity = models.IntegerField() # vaccine availability
    vaccine = models.CharField(max_length=50)
    status = models.CharField(max_length=10,default='DEFAULT') # status , NEW , OLD , COMPLETE 
    

    def __str__(self):
        return self.district_name