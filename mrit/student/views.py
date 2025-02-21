from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Students

# Create your views here.
def student_list(request):
    if request.method=='POST':
        name = request.POST.get('name')
        gender=request.POST.get('gender')
        address = request.POST.get("address")
        student=Students(name=name,gender=gender,address=address )

        student.save()
        return redirect('student_list')
    students= Students.objects.all()
    return render(request, 'index.html', {'students':students})

def add_student(request):
    if request.method=='POST':
        name = request.POST.get('name')
        gender=request.POST.get('gender')
        address = request.POST.get("address")
        student=Students(name=name,gender=gender,address=address )

        student.save()
        return redirect('student_list')
    return render(request,'index.html')
    # if request.method=='POST':
    #     name=request.POST['name']
    #     gender=request.POST['gender']
    #     address=request.POST['address']
    #     profile_pic=request.POST['profile_pic']


    #     student=Students(name=name, gender=gender, address=address, profile_pic=profile_pic)
    #     student.save()

    #     return HttpResponse(f"Post '{name}' saved")
    # students = Students.objects.all()
    # return render(request, 'index.html',{'students':students})