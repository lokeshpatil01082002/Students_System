from django.http import HttpResponse
from django.shortcuts import render
from .models import student,branch,year
# Create your views here.

def index(request):
    return render(request,'index.html')

def view(request):
    students=student.objects.all()
    context={
        'students':students
    }
    print(context)
    return render(request,'view.html',context)

def add(request):
    if request.method=='POST':
        prn=request.POST['prn']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        branch = request.POST['branch']
        year = request.POST['year']
        new_student=student(prn=prn,first_name=first_name,last_name=last_name,branch_id=branch,year_id=year)
        new_student.save()
        return HttpResponse('Student Data Added !')
    elif request.method=='GET':
        return render(request,'add.html')
    else:
        return HttpResponse('Exception Occured !!!!')
def deletef(request,student_id=0):

    if student_id:
        student_to_delete=student.objects.get(id=student_id)
        student_to_delete.delete()
        return HttpResponse('Removed !')
    students = student.objects.all()
    context = {
        'students': students
    }
    return render(request,'deletef.html',context)

def update(request,student_id=0):
    if student_id:
        student_to_update=student.objects.get(id=student_id)
        student_to_update.delete()
        return HttpResponse("Updated")

        update_data(request,student_to_update)

    students = student.objects.all()
    context = {
        'students': students
    }

    return render(request,'update.html',context)


def update_data(request,student):
    if request.method=='POST':
        prn=request.POST['prn']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        branch = request.POST['branch']
        year = request.POST['year']
        new_student=student(prn=prn,first_name=first_name,last_name=last_name,branch_id=branch,year_id=year)
        new_student.save()
        return HttpResponse('Student Data Added !')
    elif request.method=='GET':
        return render(request,'update.html')
    else:
        return HttpResponse('Exception Occured !!!!')
