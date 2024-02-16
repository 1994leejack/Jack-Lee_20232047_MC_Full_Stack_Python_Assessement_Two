from django.db import models

# Create your models here.

class RenewablePowerGeneration(models.Model):
    mode_of_generation = models.CharField(max_length=100)
    contribution_twh = models.FloatField()

    def __str__(self):
        return self.mode_of_generation
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email