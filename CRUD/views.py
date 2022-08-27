from django.shortcuts import render,redirect
from .models import register
from django.contrib import messages

# Create your views here.

# Indexpage/Homepage
def index(request):
  return render(request,"registerform.html")

# value insert to database,table
def valueinsert(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']
    register(name = name, email = email, contact = contact).save()
    messages.success(request,"Value Inserted Successfully")
    return render(request,"registerform.html")
    # return redirect ('viewlist')
  else:
    return render(request,"404.html")

# value listed from database,table
def viewlist(request):
  value = register.objects.all()
  if(value != ''):
    return render(request,"viewlist.html",{'data':value})
  else:
    return render(request,"viewlist.html")

# update value in database
def update(request, id):
  value = register.objects.get(id = id)
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']

    # tablename.rowname = name tag name  | updating/inserting values in table
    value.name = name
    value.email = email
    value.contact = contact
    value.save()
    messages.success(request,"Data Updated Successfully")
    return redirect('viewlist')

  return render(request,"updateform.html",{'data':value})

