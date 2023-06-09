from django.db import models

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    def __str__(self):
        return self.title