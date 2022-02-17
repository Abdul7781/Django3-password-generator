from django.shortcuts import render
from django.http import HttpResponse
import random
def home (request):
    return render(request, 'generator/home.html', {'password':'hjejjej33555jgfj'})

def about (request):
    return render(request, 'generator/about.html')

def contact(abdul):
    return render(abdul, 'generator/contact.html')


def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))

    if request.GET.get('special characters'):
        characters.extend(list('@#$%^&*()'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('123345678900'))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html',{'password':thepassword})
