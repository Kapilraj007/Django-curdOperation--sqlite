from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas
# Create your views here.

def registration(request):
    mydata=Datas.objects.all()
    if(mydata!=''):
        return render(request, "dbregistration.html",{'datas':mydata})
    else:
        return render(request, "dbregistration.html")


def addData(request):
    if request.method == 'POST':
        name=request.POST["name"]
        age=request.POST["age"]
        address=request.POST["address"]
        contact=request.POST["contact"]
        mail =request.POST["mail"]
        obj=Datas()
        obj.Name=name
        obj.Age=age
        obj.Contact=contact
        obj.Mail=mail
        obj.Address=address
        obj.save()
        mydata=Datas.objects.all()
        return redirect('register')
    return render(request, "dbregistration.html")

def updateData(request,id):
    mydata=Datas.objects.get(id=id)
    if request.method=='POST':
        name=request.POST["name"]
        age=request.POST["age"]
        address=request.POST["address"]
        contact=request.POST["contact"]
        mail =request.POST["mail"]
        mydata.Name=name
        mydata.Age=age
        mydata.Contact=contact
        mydata.Mail=mail
        mydata.Address=address
        mydata.save()
        return redirect('register')
    return render(request, "update.html",{'data':mydata})

def deleteData(request,id):
    mydata=Datas.objects.get(id=id) #oject(8)
    mydata.delete()
    return redirect('register')