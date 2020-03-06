from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=500)
    updatedatetime = models.DateTimeField(auto_now=True)
    createdatetime = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete =models.CASCADE ,null = True)
    def __unicode__(self):
        return self.title