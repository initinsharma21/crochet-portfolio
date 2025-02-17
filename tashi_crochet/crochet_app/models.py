from django.db import models

class CrochetImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='crochet_images/')
    
    def __str__(self):
        return self.title