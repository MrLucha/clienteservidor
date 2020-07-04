from django.db import models


# Create your models here.

class ExampleModel(models.Model):
    name=models.CharField(max_length=255,null=False);
    age=models.IntegerField(null=False);
    address=models.CharField(max_length=200,null=False);
    curp=models.CharField(max_length=16,null=False);

    def __str__(self):
        return self.name

    class Meta:
        db_table='Example1'