import email
from django.db import models


class Contact(models.Model):
    SUBJECT_CHOICES = [
        ('Order','Order'), 
        ('Return','Return'), 
        ('Delivery','Delivery')]
    subject =  models.CharField(
        choices=SUBJECT_CHOICES,
        verbose_name=("subject choice"),
        max_length=255,
    )
    name = models.CharField(max_length=250)
    email = models.EmailField()
    title = models.CharField(verbose_name='Title',max_length=250)
    message = models.TextField()
    img = models.ImageField(verbose_name='Image', width_field=200, height_field=150, upload_to='images',blank=True)
    date_send = models.DateTimeField(auto_now_add=True, blank=True)
    resolved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
