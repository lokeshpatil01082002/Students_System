from django.db import models

# Create your models here.
class branch(models.Model):
    brnachString=models.CharField(max_length=10)
    def __str__(self):
        return self.brnachString


class year(models.Model):
    yearS=models.CharField(max_length=10)
    def __str__(self):
        return self.yearS

class student(models.Model):
    first_name=models.CharField(max_length=30,null=False)
    last_name=models.CharField(max_length=30,null=False)
    address=models.CharField(max_length=100,null=False)
    prn=models.CharField(max_length=10,null=False)
    branch=models.ForeignKey(branch,on_delete=models.CASCADE)
    year=models.ForeignKey(year,on_delete=models.CASCADE)

    def __str__(self):
        return "%s  %s - %s - %s - %s"  %(self.first_name,self.last_name,self.prn,self.year,self.branch)








