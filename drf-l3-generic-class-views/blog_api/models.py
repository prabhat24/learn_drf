from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Post(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=30, unique=True, null=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save()


    def __str__(self):
        return f"Post obj : {self.title}"

    def __unicode__(self):
        return f"Post obj : {self.title}"

    class Meta:
        ordering = ['created', ]
