from django.shortcuts import render, redirect
from .models import todo
# Create your views here.
def show(request):
	data = todo.objects.all()
	return render(request, 'index.html', {'data': data})


def add(request):
    obj = todo()
    obj.title = request.POST['title']
    obj.content = request.POST['content']
    obj.save()
    mydictionary = {
        "todo" : todo.objects.all()
    }
    return redirect(show)


def deleteItem(request, todo_id):
    item = todo.objects.get(id = todo_id)
    item.delete()
    return redirect(show)


def Edit(request,id):
    obj = todo.objects.get(id=id)
    mydictionary = {
    	"title" : obj.title,
        "content" : obj.content,
        "id" : obj.id
    }
    data = todo.objects.all()
    return render(request,'edit.html',context=mydictionary)


def update(request,id):
    obj = todo(id=id)
    obj.title = request.GET['title']
    obj.content = request.GET['todoup']
    obj.save()
    
    mydictionary = {
        "content" : todo.objects.all()
    }
    
    return redirect(show)

