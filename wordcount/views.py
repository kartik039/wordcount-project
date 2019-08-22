from django.http import HttpResponse
from django.shortcuts import render
from collections import defaultdict
import operator

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'aboutme.html')

def count(request):
    textall = request.GET['text']
    text = textall.replace(',','')
    text = text.replace('.','')
    
    count = len(text.split())
    defdict = defaultdict(int)

    for i in text.split():
        defdict[i] += 1

    max = 0

    for i in defdict.keys():
        if defdict[i] >= max:
            max = defdict[i]
            maxword = i

    defdict = sorted(defdict.items(),key=operator.itemgetter(1),reverse=True)

    return render(request, 'count.html', {'text':textall,'count':count, 'defdict':defdict})