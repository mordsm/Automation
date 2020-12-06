from django.db import models


class Sites(models.Model):
    name = models.CharField(max_length=200)
    script = models.TextField()
    tree_script = models.TextField()
    site_yaml = models.TextField()


