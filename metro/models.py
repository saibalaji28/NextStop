from django.db import models

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Connection(models.Model):
    from_station = models.ForeignKey(
        Station,
        related_name="from_connections",
        on_delete=models.CASCADE
    )
    to_station = models.ForeignKey(
        Station,
        related_name="to_connections",
        on_delete=models.CASCADE
    )
    distance = models.IntegerField(help_text="Distance in minutes")

    def __str__(self):
        return f"{self.from_station} → {self.to_station} ({self.distance})"