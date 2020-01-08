from  django.db import models


class employee(models.Model):

    sno=models.CharField(max_length=50)
    sname = models.CharField(max_length=50)
    fname= models.CharField(max_length=50)
    desig=models.CharField(max_length=50)
    directno = models.CharField(max_length=50, null=True, blank=True)
    eabxno = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=10)
    emailid=models.EmailField(max_length=50, null=True, blank=True)
    office = models.CharField(max_length=50)
    def __str__(self):
        return self.fname

