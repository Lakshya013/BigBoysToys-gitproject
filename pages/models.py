from django.db import models

# Create your models here.
# on every edit we have to make a migration cmd
class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    desigination = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%y/%m/%d') # will create a folder phots inside it year,month, day
    facebook_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    google_plus_link = models.URLField(max_length=255)
    create_data = models.DateTimeField(auto_now_add=True) # the migration will make all these changes to be ready for db table 

    def __str__(self):
        return self.first_name