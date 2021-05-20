from django.db import models


# Create your models here.
class Inbox(models.Model):
    TaskId = models.AutoField(primary_key=True)
    inboxTaskName = models.CharField(max_length=500)


class PlanningPeriod(models.Model):
    planningPeriodId = models.AutoField(primary_key=True)
    scheduledPlanning = models.DateTimeField()


class SimpleTask(models.Model):
    TaskId = models.AutoField(primary_key=True)
    taskName = models.CharField(max_length=500)
    todoCheck = models.BinaryField()
    completedCheck = models.BinaryField()
    addedDate = models.DateTimeField()


class ProjectTask(models.Model):
    TaskId = models.AutoField(primary_key=True)
    taskName = models.CharField(max_length=500)
    projectName = models.CharField(max_length=500)
    todoCheck = models.BinaryField()
    completedCheck = models.BinaryField()
    addedDate = models.DateTimeField()


class Project(models.Model):
    projectId = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length=500)
    completedCheck = models.BinaryField()


