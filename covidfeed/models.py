from django.db import models

# Create your models here.


class Topic(models.Model):

    topic_name = models.CharField(max_length=264)

    def __str__(self):
        return self.topic_name

class Plasma(models.Model):
    plasma_user_name = models.CharField(max_length=50) # social media user
    plasma_topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    plasma_social_media_content = models.CharField(max_length=1024) # content of data
    plasma_request_date = models.DateField() #date created
    plasma_user_location = models.CharField(max_length=50,default=' ') # social media user


    def __str__(self):
        return self.plasma_user_name

class Oxygen(models.Model):
    oxygen_user_name = models.CharField(max_length=50) # social media user
    oxygen_topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    oxygen_social_media_content = models.CharField(max_length=1024) # content of data
    oxygen_request_date = models.DateField() #date created
    oxygen_user_location = models.CharField(max_length=50,default=' ') # social media user

    def __str__(self):
        return self.oxygen_user_name

class Bed(models.Model):
    bed_user_name = models.CharField(max_length=50) # social media user
    bed_topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    bed_social_media_content = models.CharField(max_length=1024) # content of data
    bed_request_date = models.DateField() #date created
    bed_user_location = models.CharField(max_length=50,default=' ') # social media user


    def __str__(self):
        return self.bed_user_name






