from django.db import models


class ExistCity(models.Model):
    CITY_CHOICES = (
        ('London', 'London'),
        ('Tokyo', 'Tokyo'),
        ('New York', 'New York'),
        ('Liverpool', 'Liverpool'),
        ('Kyiv', 'Kyiv'),
        ('Vinnytsia','Vinnytsia'),
        ('Las Vegas', 'Las Vegas'),
        ('Donetsk', 'Donetsk'),
        ('Lviv', 'Lviv'),
        ('Baku', 'Baku'),
        ('Moscow', 'Moscow'),
        ('Sevastopol', 'Sevastopol'),
        ('Paris', 'Paris'),
    )

    # name = models.CharField(max_length=30, choices=CITY_CHOICES, blank=True)
    # temperature = models.FloatField(default=0)
    # description = models.CharField(max_length=40,blank=True)
    # icon = models.CharField(max_length=10,blank=True)
    # date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class NewCity(models.Model):

    name = models.CharField(max_length=30)
    temperature = models.FloatField(default=0)
    description = models.CharField(max_length=40,blank=True)
    icon = models.CharField(max_length=10, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
