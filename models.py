from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)#on delete means what to do if user gets deleted
    #cascade---- means delete
    #models.SET_NULL--- set null value
    title=models.CharField(max_length=500)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    create=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['complete']    
