from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def home(request):
    todoLists={}
    if request.method == "POST":
        todos=request.POST.get("todo")
        todo.objects.create(todoName = todos)
        return redirect('/')

    todoLists['list']= todo.objects.all()
       
    return render(request,'home.html' ,todoLists)

    
def deleteList(request,id):
    try:
        todoObj= todo.objects.get(id=id).delete()
    except Exception    as e:

        print(e)
    return  redirect('/')



        

        
