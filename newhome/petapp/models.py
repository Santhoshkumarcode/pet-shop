from django.db import models

# Create your models here.
class customerdetails(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    email=models.EmailField(max_length=50,blank=False,null=False)
    breed=models.CharField(max_length=50,blank=False,null=False)
    quantity=models.PositiveIntegerField(max_length=50,blank=False,null=False)
    number=models.PositiveIntegerField(max_length=10,blank=False,null=False)
    def __str__(self):
        return self.name


class catdetails(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    email=models.EmailField(max_length=50,blank=False,null=False)
    breed=models.CharField(max_length=50,blank=False,null=False)
    quantity=models.PositiveIntegerField(max_length=50,blank=False,null=False)
    number=models.PositiveIntegerField(max_length=10,blank=False,null=False)
    def __str__(self):
        return self.name




class puppydetails(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    breed=models.CharField(max_length=50,blank=False,null=False)
    age=models.CharField(max_length=50,blank=False,null=False)
    vaccination=models.CharField(max_length=50,blank=False,null=False)
    number=models.PositiveIntegerField()
    def __str__(self):
        return self.name

        

