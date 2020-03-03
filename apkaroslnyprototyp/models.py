from django.db import models

class Guide(models.Model):
    title = models.CharField(max_length=128, null=False, unique=True)
    content = models.TextField(null=False)
    add_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    points = models.IntegerField(default=0)
    #t odo dodac jeszcze mozliwosc dodawania jpgow

class GuideComment(models.Model):
    content = models.CharField(max_length=500, null=False)
    add_date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=0)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)

class TradePost(models.Model):
    title = models.CharField(max_length=100, null=False)
    add_date = models.DateTimeField(auto_now_add=True)
    plant_name = models.CharField(max_length=128, null=True)
    is_active = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=False)
    ##t odo  dodac jeszcze jotpega jakiegs

class TradeComment(models.Model):
    content = models.CharField(max_length=500, null=False)
    add_date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=0)
    post = models.ForeignKey(TradePost, on_delete=models.CASCADE)

