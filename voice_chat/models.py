from  django.db import models


class Sites(models.Model):
    name = models.CharField(max_length=200)
    script = models.TextField()
    tree_script = models.TextField()
    site_yaml = models.TextField()


class Config(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    password = models.TextField(max_length=30)
    data = models.JSONField(default=None, blank=True, null=True)

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


