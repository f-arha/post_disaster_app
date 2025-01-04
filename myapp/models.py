from django.db import models

# Create your models here.



class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class camp_table(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    post = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    contactno= models.BigIntegerField()

class member_table(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    post = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=100)
    age = models.BigIntegerField()

class camp_co_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    image=models.FileField()

class volunteer(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    image = models.FileField()
    place = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    post = models.CharField(max_length=100)
    aadhar = models.BigIntegerField()

class dataset(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

class need(models.Model):
    COORDID = models.ForeignKey(camp_co_table, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    needs = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class donate(models.Model):
    NEEDID = models.ForeignKey(need, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class request_psychologist(models.Model):
    COORDID = models.ForeignKey(camp_co_table, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class emergency_notification(models.Model):
    ID = models.ForeignKey(need, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)