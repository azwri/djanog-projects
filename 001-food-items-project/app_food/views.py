from django.shortcuts import render, get_object_or_404
from .models import Item


def index(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'app_food/index.html', context)


def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'app_food/item_detail.html', context)