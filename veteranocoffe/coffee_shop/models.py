from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Company(models.Model):
    company_name =  models.CharField(max_length=100)    
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    map_url = models.URLField(max_length=254)  
    facebook_url = models.URLField(max_length=254)  
    instagram_url = models.URLField(max_length=254)  

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        if Company.objects.exists() and not self.pk:
            raise ValidationError('There is can be only one company')
        return super(Company, self).save(*args, **kwargs)

class News(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + '...'
    
class Publication(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='publication_images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + '...'


# Create your models here.
