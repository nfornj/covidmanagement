from django.db import models

# Create your models here.


class Topic(models.Model):

    topic_name = models.CharField(max_length=264)

    def __str__(self):
        return self.topic_name

class Location(models.Model):

    location_name = models.CharField(max_length=264)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.location_name

class Plasma(models.Model):
    user_name = models.CharField(max_length=50) # social media user
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    social_media_content = models.CharField(max_length=1024) # content of data
    request_date = models.DateField() #date created
    user_location = models.CharField(max_length=50,default=' ') # social media user
    status = models.CharField(max_length=10,default='New') # status , NEW , OLD , COMPLETE 

    def __str__(self):
        return self.user_name

class Oxygen(models.Model):
    user_name = models.CharField(max_length=50) # social media user
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    social_media_content = models.CharField(max_length=1024) # content of data
    request_date = models.DateField() #date created
    user_location = models.CharField(max_length=50,default=' ') # social media user
    status = models.CharField(max_length=10,default='New') # status , NEW , OLD , COMPLETE 

    def __str__(self):
        return self.user_name

class Bed(models.Model):
    user_name = models.CharField(max_length=50) # social media user
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    social_media_content = models.CharField(max_length=1024) # content of data
    request_date = models.DateField() #date created
    user_location = models.CharField(max_length=50,default=' ') # social media user
    status = models.CharField(max_length=10,default='New') # status , NEW , OLD , COMPLETE 


    def __str__(self):
        return self.user_name