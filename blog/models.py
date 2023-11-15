from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254,null=True, blank=True)

    def __str__(self):
        return f"{self.surname}, {self.name}"

class Poema(models.Model):
    name = models.CharField(max_length=128)
    text = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.author}"

class Cuento(models.Model):
    name = models.CharField(max_length=128)
    text = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.author}"