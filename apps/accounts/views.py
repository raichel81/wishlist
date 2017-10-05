# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login 
from django.shortcuts import render, redirect
from forms import SignUpForm

def main(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('items:dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
        