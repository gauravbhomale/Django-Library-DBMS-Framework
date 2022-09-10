from django.db import models


# Create your models here.
class Books(models.Model):
    b_id = models.IntegerField()
    book_name = models.CharField(max_length=50)

