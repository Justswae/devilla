from django.db import models
from django.contrib.auth.models import User 


class Category(models.Model):
    name = models.CharField(max_length=225)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100,blank=True, null=True)
    category = models.ForeignKey(Category, related_name= 'posts', on_delete=models.CASCADE)
    post = models.TextField(max_length=1000, blank=False, null= False)
    image = models.ImageField(upload_to='uploads',blank= True, null= True)
    created_by = models.ForeignKey(User, related_name= 'posts',on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.title