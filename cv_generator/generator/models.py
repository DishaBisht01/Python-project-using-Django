from django.db import models

class CV(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    summary = models.TextField()
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    previous_work = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return self.name
