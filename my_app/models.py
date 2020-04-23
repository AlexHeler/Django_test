from django.db import models

# Create your models here.
class  User(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    name = models.CharField(max_length=10,unique=True,null=False)
    password = models.CharField(max_length=10,null=False)
    login_num = models.IntegerField()

class  Pro(models.Model):
    pro_id = models.IntegerField(unique=True,primary_key=True)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=10,null=False)
    mail = models.EmailField(null=False)

    theme = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=3000,null=False)

class Ans(models.Model):
    ans_id = models.IntegerField(unique=True,primary_key=True)
    to_pro_id = models.IntegerField()
    user_name = models.CharField(max_length=10, null=False)
    ans_content = models.CharField(max_length=300, null=False)