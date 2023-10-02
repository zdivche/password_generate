from django.shortcuts import render
import random


def home(request): 
    return render(request, 'generator/home.html')


def password(request): 
    
    the_password = ""
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'): 
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('number'): 
        characters.extend(list('1234567890'))
        
    if request.GET.get('special'): 
        characters.extend(list('!"№;%:?*()_+!@#$%^&*()_+'))    
    length = int(request.GET.get('length', 12))
    
    
    
    for i in range(length): 
        the_password += random.choice(characters)
    
    
    return render(request, 'generator/password.html', {'password': the_password})