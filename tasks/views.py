from django.shortcuts import render,HttpResponse, redirect
# importimg Models
from .models import  Task
# importing Forms
from .forms import *
# Create your views here.
def index(request):
    
    tasks = Task.objects.all()


    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}

    return render(request,'tasks/lists.htm', context) 

# Updating Task
def upateTask(request,pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request,'tasks/update_task.htm', context)

# Deleting Task
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request,'tasks/delete.htm',context)
