from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    sentiment = models.CharField(max_length=10, default="Neutral")
    resolved = models.BooleanField(default=False)
    # Optional: add created_at to show review date
    created_at = models.DateTimeField(auto_now_add=True)
