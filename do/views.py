from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TacheForm
# Create your views here.

def index(request):
    form = TacheForm(request.POST or None)
    if form.is_valid():
        form.save()
    content = Task.objects.all()
    return render(request, 'index.html', {'taches':content, 'form':form})


def update(request, pk):
    obj = get_object_or_404(Task, id=pk)
    form = TacheForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form })
    
           



def delete(request, pk):
    obj = get_object_or_404(Task, id=pk)
    obj.delete()
    return redirect('/')              
     