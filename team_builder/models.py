from django.db import models

# Model for Units
class Unit(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='units/')
    description = models.TextField()

    def __str__(self):
        return self.name

# Model for Teams
class Team(models.Model):
    name = models.CharField(max_length=100)
    units = models.ManyToManyField(Unit)
    size_limit = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# Model for Boss Strategies
class Strategy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.title
