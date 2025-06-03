from django.db import models
from django.utils.text import slugify

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  slug = models.SlugField(blank=True, null=False)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

  def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(f"{self.firstname} {self.lastname}")
    super().save(*args, **kwargs)