from django.db import models


class Diet(models.Model):

    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    diet_data = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return f"diet data autho: {self.author} pk: {self.pk}"
