from django.db import models

class Report(models.Model):   
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title
