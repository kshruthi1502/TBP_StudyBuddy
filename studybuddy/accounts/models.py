from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
class Course(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    coursename = models.CharField(max_length=200)
    def __str__(self):
        return str(self.user) + " - " + self.coursename
class Post(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_content = models.CharField(max_length=5000)
    post_id = models.AutoField
    timestamp= models.DateTimeField(default=now)
    def __str__(self):
        return str(self.user1) + " - " + str(self.post_content) + " - "+str(self.post_id)+ " - "+str(self.timestamp)
class Replie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    reply_content = models.CharField(max_length=5000) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    timestamp= models.DateTimeField(default=now)
    def __str__(self):
        return str(self.user) + " - " + str(self.reply_content) + " - "+str(self.post) + " - "+str(self.timestamp) 

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
    def __str__(self):
        return str(self.user) + " - " + str(self.title) + " - "+str(self.content) + " - "+str(self.created_at) + " - "+str(self.modified_at) 
    
class Student(models.Model ):
    review = models.CharField(max_length=255)
    label = models.IntegerField()

    def __str__(self):
        return str(self.review) + " - " + str(self.label) 
            

   