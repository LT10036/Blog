from django.db import models

# Create your models here.

# 博 主 个 人 资 料
from django.db  import models

class author (models.Model):
    name=models.CharField(max_length=10)
    tel=models.CharField(max_length=11,default='电话号码')
    age=models.IntegerField()
    sex=models.BooleanField()
    crt_time=models.DateTimeField()

    class Meta:
        db_table='AdminInfo'
        verbose_name_plural='博主资料'

    def __str__(self):

        return self.name



class viewpoint(models.Model):
    theme=models.CharField(max_length=40,unique=True)
    content=models.TextField(max_length=4400)
    author=models.ForeignKey(author,on_delete=True)

    class Meta:
        db_table='viewpoint'
        verbose_name_plural='帖子'

    def __str__(self):
        return self.theme




class visitor(models.Model):
    name=models.CharField(max_length=10)
    open_id=models.CharField(max_length=10)
    age=models.IntegerField()
    sex=models.BooleanField()

    class Meta:
        db_table='visitor'

        verbose_name_plural='访客资料'

    def __str__(self):
        return  self.name




class visitorhistory(models.Model):
    name=models.CharField(max_length=10)
    historytime=models.DateTimeField()

    class Meta:
        db_table='vth'

        verbose_name_plural='访客记录'



