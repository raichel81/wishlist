# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewItemForm

from .models import Item

def dashboard(request):
    if request.user.is_authenticated:
        myitems = request.user.items.all()
        user = request.user
        othersitems = Item.objects.all().exclude(users=user)
        context={
            'othersitems' : othersitems,
            'myitems' : myitems
        }    
        return render(request, 'dashboard.html', context)
    else:
        return redirect('accounts:main')

def wish_items(request, pk):
    item = Item.objects.get(id = pk)
    context={
        'item' : item
    }
    return render(request, 'item.html', context)

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = NewItemForm(request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.created_by_id = request.user.id
                item.save()
                item.users.add(request.user)
                return redirect('items:dashboard')  
        else:
            form = NewItemForm()
        return render(request, 'create.html', {'form': form})
    else:
        return redirect('items:dashboard')

def add(request, pk):
    if request.user.is_authenticated:
        item= Item.objects.get(id = pk)
        user = request.user
        item.users.add(user)
    return redirect('items:dashboard')

def delete(request, pk):
    if request.user.is_authenticated:
        item= Item.objects.get(id = pk)
        item.delete()
    return redirect('items:dashboard')

def remove(request, pk):
    if request.user.is_authenticated:
        item= Item.objects.get(id = pk)
        user = request.user
        item.users.remove(user)
    return redirect('items:dashboard')