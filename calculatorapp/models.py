from django.db import models
from django.urls import reverse 
class Calculatort(models.Model):
   expression = models.CharField(max_length = 50)
   results = models.IntegerField()
   
   def __str__(self):
        return self.num1
   def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])
   
         


