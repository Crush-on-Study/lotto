from django.db import models

class Lotto(models.Model):
    draw_number = models.IntegerField()
    numbers = models.CharField(max_length=255)

    def __str__(self):
        return f"Lotto {self.draw_number}"

# Create your models here.