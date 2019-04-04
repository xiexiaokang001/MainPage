from django.shortcuts import render
from django.http import HttpResponse

def ascii(request):
    return render(request,'ascii.html')

def asciisubmit(request):
    context = {'result':"显示一下"}
    return render(request,'ascii.html', context=context)