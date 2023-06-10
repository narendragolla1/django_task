from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/', null=True, blank=True)
    active=models.BooleanField(default=False)
    
        
    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super(Product,self).delete(*args, **kwargs)
