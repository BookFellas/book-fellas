from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import date, datetime, timedelta

STATUSES = (
    ('Complete', 'Complete Order'),
    ('Pending', 'Pending Order'),
    ('Canceled', 'Canceled Order'),
    ('Empty', 'Empty Cart'),
)

class Book(models.Model):
    isbn = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year_published = models.CharField(max_length=15, default='2010')
    author = models.CharField(max_length=150)
    publisher = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    pages = models.IntegerField()
    categories = models.CharField(max_length=150)
    price = models.FloatField()
    quantity = models.IntegerField()
    book_img = models.URLField(max_length=400, blank=True)

    def __str__(self):
        return self.title
        
class Order(models.Model):
    order_date = models.DateField(auto_now=True)
    shipping_date = models.DateField(default=datetime.now()+timedelta(days=7))
    # status = models.CharField(
    #                         max_length=10,
    #                         choices=STATUSES,
    #                         default=STATUSES[0][0]
    #                     )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ProductItem(models.Model):
    quantity = models.IntegerField()
    price = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)
    
class Profile(models.Model):
    phone = models.CharField(max_length=25, null=True)
    address = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=12, null=True)
    city = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    birthday = models.DateField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profiles_index')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()