from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def topic_model(request):
    to=input('enter topic')
    To=Topic.objects.get_or_create(topics_name=to)[0]
    return HttpResponse('inserted successfully')
    to.save()

def WebPages_model(request):
    tn=input('enter topic name')
    n=input('entet name')
    url=input('enter url')
    TO1=Topic.objects.get_or_create(topics_name=tn)[0]
    wo=WebPages.objects.get_or_create(topics_name=TO1,name=n,url=url)[0]
    return HttpResponse('success')
    TO1.save()
    wo.save()
    TO2=Topic.objects.get_or_create(topics_name=TO2)[0]
    wo=WebPages.objects.get_or_create(topics_name=TO2,name=n,url=url)[0]
    To2.save()
    wo.save()

def access_insert(request):
     TO2=input('enter tn')
     n=input('enter name')
     url=input('enter url')
     aut=input('enter author')
     da=input('enter date')
     TO2=Topic.objects.get_or_create(topics_name=TO2)[0]
     WO2=WebPages.objects.get_or_create(topics_name=TO2,name=n,url=url)[0]
     AR=AcessRecords.objects.get_or_create(name=WO2,author=aut,date=da)[0]
     TO2.save()
     WO2.save()
     AR.save()
     return HttpResponse('AcessRecords created successfully')


def display_topic(request):
    TON=Topic.objects.all()
    d={'topic':TON}
    return render(request,'display_topic.html',d)

def web_display(request):
    TON=WebPages.objects.all()
    d={'web_page':TON}
    return render(request,'web_display.html',d)

def acc_display(request):
    TON=WebPages.objects.all()
    d={'access':TON}
    return render(request,'acc_display.html',d) 


