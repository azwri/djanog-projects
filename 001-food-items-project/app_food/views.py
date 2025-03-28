from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm


def index(request):
    items = Item.objects.filter(is_deleted=False)
    context = {
        'items': items
    }
    return render(request, 'app_food/index.html', context)


def detail(request, id):
    item = get_object_or_404(Item, pk=id)
    context = {
        'item': item
    }
    return render(request, 'app_food/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_food:index')
    else:
        form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'app_food/form.html', context)

def update(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('app_food:detail', id=item.id)
    else:
        form = ItemForm(instance=item)
    context = {
        'form': form,
        'item': item
    }
    return render(request, 'app_food/form.html', context)

def delete(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        # soft delete
        item.is_deleted = True
        item.save()
        return redirect('app_food:index')