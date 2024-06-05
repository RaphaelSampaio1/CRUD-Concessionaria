from django.shortcuts import render, redirect
from app.forms import carrosForm
from app.models import carros
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    
    if search:
        car_list = carros.objects.filter(modelo__icontains=search)
    else:
        car_list = carros.objects.all()
    
    paginator = Paginator(car_list, 20)
    page = request.GET.get('page')
    data['db'] = paginator.get_page(page)
    data['search'] = search
    
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = carrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = carrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk): 
    data = {}
    data['db'] = carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = carros.objects.get(pk=pk)
    data['form'] = carrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = carros.objects.get(pk=pk)
    form = carrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(request,pk):
    db = carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')
