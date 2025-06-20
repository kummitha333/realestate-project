from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import Register 
from .models import Property
from decimal import Decimal
from django.core.exceptions import ValidationError


import mysql.connector as sql


def welcome(request):
    
  return render(request, 'welcome.html')
    

def signup(request):
    global fn,pwd
    if request.method=="POST":
        s=sql.connect(host="localhost",user="root",password="root",database="project")   
        cursor=s.cursor()
        username= request.POST.get('username','')
        password= request.POST.get('password','')
            
                
        query="insert into signup (username,password) values ( %s,%s)"
        values=(username,password)
        cursor.execute(query,values)
        
        s.commit()
        s.close()
       
       
        return render(request, 'index.html')
        
    return render(request, 'signup.html')
    
def index(request):
    return render(request, 'index.html')
def residential(request):
    return render(request, 'residential.html')
def p1(request):
    return render(request, 'p1.html')
def p2(request):
    return render(request, 'p2.html')
def p3(request):
    return render(request, 'p3.html')
def p4(request):
    return render(request, 'p4.html')
def l1(request):
    return render(request, 'l1.html')
def l2(request):
    return render(request, 'l2.html')
def l3(request):
    return render(request, 'l3.html')
def l4(request):
    return render(request, 'l4.html')
def register(request):
    if request.method == "POST":
        s=sql.connect(host="localhost",user="root",password="root",database="project")   
        cursor=s.cursor()
        fullname = request.POST.get('fullname','') 
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        mobilenumber = request.POST.get('mobilenumber','')
        propertyName = request.POST.get('propertyName','')
        query="insert into register (fullname,email,password,mobilenumber,propertyName) values ( %s,%s,%s,%s,%s)"
        values=(fullname,email,password,mobilenumber,propertyName)
        cursor.execute(query,values)
        
        s.commit()
        s.close()

        return render(request, 'sucs.html')
    
    return render(request, 'register.html')

   
def transaction(request):
     if request.method == "POST":
        s=sql.connect(host="localhost",user="root",password="root",database="project")   
        cursor=s.cursor()
        fromaccount = request.POST.get('fromaccount','') 
        toaccount = request.POST.get('toaccount','')
        amount = request.POST.get('amount','')
        note = request.POST.get('note','')
     
        query="insert into transaction (fromaccount,toaccount,amount,note ) values ( %s,%s,%s,%s)"
        values=(fromaccount,toaccount,amount,note)
        cursor.execute(query,values)
        
        s.commit()
        s.close()

        return render(request, 'sucs.html')
     return render(request, 'transaction.html')
   
def com(request):
    return render(request, 'com.html')
def c1(request):
    return render(request, 'c1.html')
def c2(request):
    return render(request, 'c2.html')
def contact(request):
    return render(request, 'contact.html')
def loan(request):
    return render(request, 'loan.html')

def add_property(request):
        
    if request.method == "POST":
        s=sql.connect(host="localhost",user="root",password="root",database="project")   
        cursor=s.cursor()
        propertytype = request.POST.get('propertytype','')
        location = request.POST.get('location','')
        price = request.POST.get('price','')
        area_sqft = request.POST.get('area_sqft','') or None
        dwellingplace = request.POST.get('dwellingplace','')

        query="insert into add_property (propertytype,location,price,area_sqft,dwellingplace) values ( %s,%s,%s,%s,%s)"
        values=(propertytype,location,price,area_sqft,dwellingplace)
        cursor.execute(query,values)
        
        s.commit()
        s.close()

        return render(request, 'sucs.html')

    return render(request, 'addpro.html')

    
   
   
def documental(request):
    if request.method == "POST":
        s=sql.connect(host="localhost",user="root",password="root",database="project")   
        cursor=s.cursor()
        buyerName = request.POST.get('buyerName','')
        buyerAddress = request.POST.get('buyerName','')
        sellerName = request.POST.get('sellerName','')
        sellerAddress = request.POST.get('sellerAddress','') 
        buyerSignature = request.POST.get('buyerSignature','')
        sellerSignature = request.POST.get(' sellerSignature','')
        query="insert into documental (buyerName,buyerAddress,sellerName,sellerAddress,buyerSignature,sellerSignature ) values ( %s,%s,%s,%s,%s,%s)"
        values=(buyerName,buyerAddress,sellerName,sellerAddress,buyerSignature,sellerSignature )
        cursor.execute(query,values)
        
        s.commit()
        s.close()

        return render(request, 'sucs.html')

  

    return render(request, 'documental.html')