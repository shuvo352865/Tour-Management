from django.db import models

# Create your models here.
class calculate(models.Model):
    frm =models.CharField(max_length=100)

    destination=models.CharField(max_length=100)
    transport=models.CharField(max_length=100)
    hotel=models.CharField(max_length=100)
    person=models.FloatField()
    day=models.FloatField()
    def __str__(self):
        return self.frm