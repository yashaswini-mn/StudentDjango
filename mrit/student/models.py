from django.db import models

# Create your models here.
class Students(models.Model):
    id=models.AutoField(primary_key=True)
    gender=models.CharField(max_length=10)
    name=models.TextField()
    dob=models.DateField()
    address=models.TextField()

    def __str__(self):
        return self.name