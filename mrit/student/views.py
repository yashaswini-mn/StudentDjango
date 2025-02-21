from django.shortcuts import render
from django.http import HttpResponse
from .models import Students

# Create your views here.
def student_list(request):
    if request.method=='POST':
        name=request.POST['name']
        gender=request.POST['gender']
        dob=request.POST['dob']
        addres=request.POST['address']

        student=Students(name=name, gender=gender, dob=dob, addres=addres)
        student.save()

        return HttpResponse(f"Post '{name}' saved")
    students = Students.objects.all()
    return render(request, 'index.html',{'students':students})