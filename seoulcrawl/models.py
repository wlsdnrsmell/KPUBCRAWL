from django.db import models
from django.utils import timezone

class info_client(models.Model):
    firstname = models.CharField(max_length = 10)
    lastname = models.CharField(max_length = 10)
    email = models.CharField(max_length = 100)
    text = models.TextField(null=True)
    join_date = models.DateTimeField(
        default = timezone.now)
    def submit(self):
        self.save()
    
