from django.shortcuts import render,redirect
from .forms import BooksForm
from . models import Books
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='log_url')
def bookView(request):
    form = BooksForm()
    template_name = 'app1/add.html'
    if request.method =='POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form':form}
    return render(request, template_name, context)


@login_required(login_url='log_url')
def showBook(request):
    data = Books.objects.all()
    template_name = 'app1/show.html'
    context = {'data':data}
    return render(request, template_name, context)

def updateOrder(request,pk):
    obj = Books.objects.get(id=pk)
    form = BooksForm(instance=obj)
    template_name = 'app1/add.html'
    if request.method == 'POST':
        form = BooksForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context ={'form':form}
    return render(request, template_name, context)

def deleteOrder(request,pk):
    obj = Books.objects.get(id=pk)
    if request.method =='POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'app1/confirm.html'
    context ={'data':obj}
    return render(request, template_name, context)
