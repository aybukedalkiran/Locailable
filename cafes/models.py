from django.db import models

class Business(models.Model):
    cafeId = models.IntegerField()
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    capacity = models.IntegerField()
    available_capacity = models.IntegerField()
    image = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.name + " capacity: " + str(self.available_capacity)
