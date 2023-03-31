from django.db import models

# Create your models here.
class MetGold(models.Model):
    func=models.TextField()
    left=models.FloatField()
    right=models.FloatField()
    exp=models.FloatField()
    dir=models.CharField(max_length=3)


class MetPolPod(models.Model):
    func=models.TextField()
    left=models.FloatField()
    right=models.FloatField()
    exp=models.FloatField()
    dir=models.CharField(max_length=3)
    
class MetSven(models.Model):
    func=models.TextField()
    x=models.FloatField()
    exp=models.FloatField()
    dir=models.CharField(max_length=3)
    
class MetFib(models.Model):
    func=models.TextField()
    left=models.FloatField()
    right=models.FloatField()
    exp=models.FloatField()
    dir=models.CharField(max_length=3)
    
class MetKonfig(models.Model):
    func=models.TextField()
    x_start=models.TextField()
    delta=models.TextField()
    alpha=models.FloatField()
    landa=models.FloatField()
    exp=models.FloatField()
    dir=models.CharField(max_length=3)
    
class MetNap(models.Model):
    func=models.TextField()
    x_start=models.TextField()
    n=models.IntegerField()
    exp=models.FloatField()
    dir=models.CharField(max_length=3)
    
class MetRan(models.Model):
    func=models.TextField()
    x_start=models.TextField()
    nk=models.IntegerField()
    M=models.IntegerField()
    N=models.FloatField()
    alpha=models.FloatField()
    beta=models.FloatField()
    t=models.FloatField()
    R=models.FloatField()
    dir=models.CharField(max_length=3)
    
class MetDef(models.Model):
    func=models.TextField()
    x_vershyny=models.TextField()
    n=models.IntegerField()
    alpha=models.FloatField()
    beta=models.FloatField()
    exp=models.FloatField()
    hamma=models.FloatField()
    dir=models.CharField(max_length=3)