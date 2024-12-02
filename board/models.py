from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

#class UserProfile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#    phone_number = models.CharField(max_length=15, blank=True, null=True)
#    address = models.TextField(blank=True, null=True)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)



    def __str__(self):
        return f"Profile of {self.user.username}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def active_abs_count(self):
        return self.ads.filter(is_active=True).count()

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='ads', on_delete=models.CASCADE)

    def short_description(self):
        """Повертає короткий опис (до 50 символів)."""
        return self.description[:50] + '...'

    def description_if_old(self):
        """Деактивація оголошення, якщо минуло більше 30 днів."""
        if self.created_at < timezone.now() - datetime.timedelta(days=30):
            self.is_active = False
            self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def comment_count(self):
        return self.ad.comment_set.count()

    def __str__(self):
        return f'Comment by {self.user.user.username} on {self.ad.title}'






