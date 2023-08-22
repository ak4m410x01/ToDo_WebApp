from django.db import models
from django.utils.text import slugify

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, editable=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
