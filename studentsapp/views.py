from django.shortcuts import render
from studentsapp.models import student

def listone(request):
    try:
        unit = student.objects.get(cName='Student One')
    except:
        errormessage = "Cannot read the record"
    return render(request, "listone.html", locals())

def listall(request):
    students = student.objects.all().order_by('id')
    return render(request, "listall.html", locals())

def insert(request):
    cName = "Student Three"
    cSex = "M"
    cBirthday = "2001-02-03"
    cEmail = "studentthree@students.com"
    cPhone = "1234567892"
    cAddr = "Address 3456"
    unit = student.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail, cPhone=cPhone, cAddr=cAddr)
    unit.save()
    students = student.objects.all().order_by('-id')
    return render(request, "listall.html", locals())

def modify(request):
    unit = student.objects.get(cName="Student Three")
    unit.cBirthday = '2001-02-04'
    unit.cAddr = "Address 4567"
    unit.save()
    students = student.objects.all().order_by('-id')
    return render(request, "listall.html", locals())

def delete(request, id=None):
    unit = student.objects.get(cName='Student Three')
    unit.delete()
    students = student.objects.all().order_by('-id')
    return render(request, "listall.html", locals())
