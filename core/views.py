from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

import hashlib
import random
import string


from .forms import ImageUserForm
from .models import ImageUser

def home(request):
    
    context = {}
    return render(request, 'home.html', context)


def idImage():

    id_img = ""
    for i in range(10):
        id_img = id_img + random.choice(string.ascii_letters)
    id_img = hashlib.sha256(id_img.encode()).hexdigest()
    return id_img


def carregarImg(request):
    form = ImageUserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.id_image = idImage()
        instance.save()        
        return redirect(reverse('core:simulador') + '?img=' + instance.id_image)  
        
    context = {              
        'form': form,
    }
    return render(request, 'forms.html', context)


def simulador(request):

    id_img = request.GET.get('img', False)
    query = ImageUser.objects.filter(id_image=id_img)
    q = query.values('image')[0]['image']
    user_img = q[q.find('/')+1 : ]

    context = {
        'user_img': user_img,
    }

    return render(request, 'simulador.html', context)
