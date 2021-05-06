from django.db import models

# Create your models here.


class PlasmaTopic(models.Model):

    plasma_topic_name = models.CharField(max_length=264)

    def __str__(self):
        return self.plasma_topic_name


class Plasma(models.Model):


    plasma_user_name = models.CharField(max_length=50) # social media user
    plasma_topic_name = models.ForeignKey(PlasmaTopic,on_delete=models.CASCADE)
    social_media_content = models.CharField(max_length=1024) # content of data
    social_media = models.CharField(max_length=25) ##twitter, facebook etc... 
    plasma_request_date = models.DateField() #date created


    def __str__(self):
        return self.plasma_user_name





