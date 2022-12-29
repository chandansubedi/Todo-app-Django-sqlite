from django.db import models

# Create your models here.

class todo(models.Model):
    todoName=models.CharField(max_length=100)
    isCompleted=models.BooleanField(default=False)
    createAt=models.DateField(auto_now_add=True)


    def __str__(self):
        
        return self.todoName
