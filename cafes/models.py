from django.db import models

class Cafe:
    cafeId = models.UUIDField
    name = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=100)
    capacity = models.IntegerField()
    available_capacity = models.IntegerField




class Business(models.Model):
    businessId = models.UUIDField()
    numpages = models.IntegerField()

    Cafe = models.ManyToManyField(Cafe,
                                     on_delete=models.CASCADE,
                                     null=True,
                                     blank=True
                                     )

    def __str__(self):
        return self.title + " pp. " + str(self.numpages)

class rate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    books = models.ManyToManyField(Cafe)

    class Meta:
        ordering = ['firstname', 'lastname']

    def __str__(self):
        return self.firstname + " " + self.lastname
