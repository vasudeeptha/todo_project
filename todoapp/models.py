from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE, blank=True,null=True)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=500,blank=True,null=True)
    complete = models.BooleanField(default=False)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category,on_delete= models.CASCADE,default="general")

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

