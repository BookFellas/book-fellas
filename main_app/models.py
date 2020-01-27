from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import date

class Book(models.Model):
    isbn = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year_published = models.CharField(max_length=15, default='2010')
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=30)
    price = models.FloatField()
    quantity = models.IntegerField()
    book_img = models.URLField(max_length=350, blank=True)
    

    def __str__(self):
        return self.title

class Cart(models.Model):
    order_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    quantity = models.IntegerField()
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.user

class Profile(models.Model):
    phone = models.CharField(max_length=25,null=True)
    address = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=12, null=True)
    city = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    birthday = models.DateField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()