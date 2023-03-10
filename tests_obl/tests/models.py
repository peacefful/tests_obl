from django.db import models

class School(models.Model):
    name = models.CharField(max_length=50)


class Group(models.Model):
    name = models.CharField(max_length=15)
    school = models.CharField(max_length=50)


class Subject(models.Model):
    name = models.CharField(max_length=15)
    school = models.CharField(max_length=50)


class Test(models.Model):
    name = models.CharField(max_length=15)
    school = models.CharField(max_length=50)
    subject = models.CharField(max_length=15)


class TestVersion(models.Model):
    name = models.CharField(max_length=15)
    test = models.CharField(max_length=50)


class TestQuestion(models.Model):
    test_version = models.CharField(max_length=15)
    max_points = models.IntegerField(max_length=50)