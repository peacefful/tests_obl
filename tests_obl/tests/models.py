from django.db import models

class School(models.Model):
    name = models.CharField(max_length=50)


class Group(models.Model):
    name = models.CharField(max_length=15)
    school = models.ManyToManyField(School)


class Subject(models.Model):
    name = models.CharField(max_length=15)
    school = models.ManyToManyField(School)


class Test(models.Model):
    name = models.CharField(max_length=15)
    school = models.ManyToManyField(School)
    subject = models.ManyToManyField(Subject)


class TestVersion(models.Model):
    name = models.CharField(max_length=15)
    test = models.ManyToManyField(name)


class TestQuestion(models.Model):
    test_version = models.ManyToManyField(TestVersion)
    max_points = models.IntegerField()