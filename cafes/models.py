from django.db import models

class Business(models.Model):
    title = models.CharField(max_length=200)
    numofpages = models.IntegerField()
    # publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + "pp. " + str(self.numofpages)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    cafes = models.ManyToManyField(Business)

