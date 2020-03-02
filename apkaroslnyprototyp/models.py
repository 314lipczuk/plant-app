from django.db import models

# Create your models here.
class Guide(models.Model):
    title = models.CharField(max_length=128, null=False, unique=True)
    content = models.TextField(null=False)
    add_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    points = models.IntegerField(default=0)


class GuideComment(models.Model):
    title = models.CharField(max_length=64, null=False, unique=True)
    content = models.CharField(max_length=500, null=False)
    add_date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=0)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)



