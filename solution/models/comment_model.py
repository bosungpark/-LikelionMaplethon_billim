from django.db import models
from django.conf import settings

class Comment(models.Model):
    solution_id = models.ForeignKey("Solution", on_delete=models.CASCADE, db_column="solution_id")
    comment_id = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()