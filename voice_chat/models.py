import django.db


class Sites(django.db.models.Model):
    name = django.db.models.CharField(max_length=200)
    script = django.db.models.TextField()
    tree_script = django.db.models.TextField()
    site_yaml = django.db.models.TextField()


class Config(django.db.models.Model):
    name = django.db.models.CharField(max_length=30)
    code = django.db.models.CharField(max_length=30)
    password = django.db.models.TextField(max_length=30)
    data = django.db.models.JSONField(default=None, blank=True, null=True)

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


