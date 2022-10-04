from operator import delitem

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.functions import Now
from datetime import timedelta , datetime


# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name



class PostModel(models.Model):
    title = models.CharField(max_length=255)
    head_image = models.ImageField(upload_to="upload/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text =RichTextField(blank=True,null=True)
    postdate = models.DateTimeField(auto_now_add=True, db_index=True)



    def __str__(self):
        return self.title + '|' + str( self.user) 


    def get_absolute_url(self):
        return reverse("index")

    def get_delete (self,*args,**options):
        PostModel.objects.filter(Posting_delete__lte=datetime.Now()-timedelta(minets=1)).delete()
        



class CommentModel(models.Model):
    pro = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name="comments",null=True,blank=True)
    name = models.CharField(null= True, blank=True, max_length=255)
    comm = models.TextField(null=True, blank=True)
    comment_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s - %s - %s' % (self.pro, self.name, self.comm)
        
 
     