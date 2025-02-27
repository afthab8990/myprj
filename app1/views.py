from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Students

def home(request):
    sdata = Students.objects.all()
    context = {'ses' : request.session.get('name_s'),
               'sdata' :sdata}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def row(request):
    return render(request,'row.html')

def body(request):
    return render(request,'body.html')

def login(request):
    return render(request,'login.html')

def addstudent(request):
    if request.method=='POST':
        name = request.POST['name']
        rollno = request.POST['rollno']
        data = Students(name=name, rollno=rollno)
        data.save()
    return redirect(home)

def editstudents(request,id):
    sdata = Students.objects.filter(id=id)
    return render(request,'edit.html',{'sdata':sdata})

def updatestudents(request,id):
        if request.method=='POST':
            name = request.POST.get('name')
            rollno = request.POST.get('rollno')
            Students.objects.filter(id=id).update(name=name,rollno=rollno)
        return redirect(home)

def deletestudents(request,id):
     ndata = Students.objects.filter(id=id)
     ndata.delete()
     return redirect(home)

def studentsession(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        if Students.objects.filter(name=name, rollno=rollno).exists():
            data = Students.objects.filter(name=name, rollno=rollno).values('name', 'rollno', 'id').first()
            request.session['name_s'] = data['name']
            request.session['rollno_s'] = data['rollno']
            request.session['s_id'] = data['id']
            return redirect('home')
        else:
            return render(request, 'login.html', {'msg': 'Wrong credentials or not verified'})
    else:
        return redirect('login')
    
def logout(request):
    request.session.flush()
    return redirect(login)
# Create your views here.
