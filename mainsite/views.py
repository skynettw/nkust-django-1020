from django.shortcuts import render
from django.http import HttpResponse
import random

def homepage(request):
    lottos = list()
    for i in range(6):
        lottos.append(random.randint(1, 42))

    return render(request, "index.html", locals())
    
