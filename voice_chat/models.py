from jsonfield import JSONField
from django.contrib.postgres.fields.jsonb import JSONField
from  django.db import models
#from django.db.models import JSONField

class Sites(models.Model):
    name = models.CharField(max_length=200)
    script = models.TextField()
    tree_script = models.TextField()
    site_yaml = models.TextField()

class Work(models.Model):
    work_done = models.CharField(max_length=150, null=True, blank=True)
    how_done = models.CharField(max_length=150, null=True, blank=True)
    learn  = models.CharField(max_length=150, null=True, blank=True)
    work_next = models.CharField(max_length=150, null=True, blank=True)
    how_next = models.CharField(max_length=150, null=True, blank=True)
    code = models.TextField(max_length=500, null=True, blank=True)


class Config(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    password = models.TextField(max_length=30)
    data = models.TextField(max_length=300, null=True, blank=True)

    def get_code(self):
        return self.code
    def get_password(self):
        return self.password
    @property
    def auth(self):
        #"Returns the person's authentication."
        return {"code":self.code, "password":self.password}
    def __str__(self):
        return self.name


