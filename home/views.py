from django.shortcuts import render
from .models import Category,Products


def index(request):
    data=Category.objects.all()
    return render(request,"index.html",{"pro":data})

def category(request):
    id=request.GET["id"]
    category=Category.objects.get(id=id)
    data=Products.objects.filter(pro_id=id)
    return render(request,"category.html",{"category":data})

def detail(request):
    id=request.GET["id"]
    data=Products.objects.filter(id=id)
    return render(request,"details.html",{"pro":data})

def address(request):
    if request.method=="POST":
        id=request.GET["id"]
        quantity=request.POST["quantity"]
        print(quantity)
        data=Products.objects.filter(id=id)
        print(id)
    
    return render(request,"address.html",{"pro":data,"quantity":quantity})

def final(request):
    id=request.GET["id"]
    if request.method=="POST":
        name=request.POST["name"]
        address=request.POST["address"]
        phn=request.POST["number"]
        code=request.POST["code"]
        quantity=request.POST["quantity"]
        payment=request.POST["Payment"]
        data=Products.objects.filter(id=id)
        bata=Products.objects.get(id=id)
        t=int(bata.price)-(int(bata.price)*int(bata.discount)/100)
        total=t*int(quantity)
    return render(request,"final.html",{"pro":data,"name":name,"address":address,"phn":phn,"code":code,"quantity":quantity,"total":total,"payment":payment})





















def bill(request):
    id=request.GET["id"]
    if request.method=="POST":
        quantity=request.POST["a"]
        print(quantity)
        print(id)
        data=Products.objects.get(id=id)
        
        total=int(quantity)*int(data.price)
        print(total)
        return render(request,"bill.html",{"bill":total,"data":data,"quantity":quantity})
    

 

