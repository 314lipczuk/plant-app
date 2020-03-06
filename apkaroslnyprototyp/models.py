from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.user_id)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Guide(models.Model):
    title = models.CharField(max_length=128, null=False, unique=True)
    content = models.TextField(null=False)
    add_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    points = models.IntegerField(default=0)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    #t odo dodac jeszcze mozliwosc dodawania jpgow

class GuideComment(models.Model):
    content = models.CharField(max_length=500, null=False)
    add_date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=0)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
class TradePost(models.Model):
    title = models.CharField(max_length=100, null=False)
    add_date = models.DateTimeField(auto_now_add=True)
    plant_name = models.CharField(max_length=128, null=True)
    is_active = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=False)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(null=True)
    ##t odo  dodac jeszcze jotpega jakiegs

class TradeComment(models.Model):
    content = models.CharField(max_length=500, null=False)
    add_date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=0)
    post = models.ForeignKey(TradePost, on_delete=models.CASCADE)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)


