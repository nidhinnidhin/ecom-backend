from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    email = models.EmailField(null = True, blank = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.username

class ForgetPasswordOTP(models.Model):
    otp = models.CharField(max_length = 4)
    created_on = models.DateTimeField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username


class UserProfileEmailEdit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.user.username