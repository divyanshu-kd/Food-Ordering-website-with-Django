from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=150,null=True)
    receipe_description = models.TextField(null=True)
    receipe_image = models.ImageField(upload_to="Media",null=True)
