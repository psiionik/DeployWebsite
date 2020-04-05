from django.db import models

# Create your models here.
class Subscription(models.Model):
    title = models.CharField(max_length=200, blank=False, primary_key=True)

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

