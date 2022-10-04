from django.db import models

class Instructor(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructor'

class Trainer(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainer'


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    img = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gallery'
