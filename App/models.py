from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

# Create your models here.


class Phone(models.Model):
    phone_no = models.CharField(max_length=10)
    user_id = models.OneToOneField(User,on_delete=CASCADE)

    def __str__(self):
        return self.phone_no



