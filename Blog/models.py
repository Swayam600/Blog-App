from django.db import models

# Create your models here.

class Post(models.Model):
    Username = models.CharField(max_length=100)
    Title = models.CharField(max_length=300)
    Content = models.TextField()
    Date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Title

    def slug(self):
        return self.Content[:500]



    

    
