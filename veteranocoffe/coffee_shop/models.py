from PIL import Image
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200] + '...'
    



class Publication(News):
    pass

# Create your models here.
