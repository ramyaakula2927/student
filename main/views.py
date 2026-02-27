from django.shortcuts import render
from main.models import Student

def home(request):
    return render(request, 'main/home.html')


def colleges(request):
    collegelist = ['SVECW', 'VIT', 'BVRICE']
    
    return render(request, 'colleges.html', {'colleges': collegelist})





def student(request):  
    studentdata=Student.objects.all()
    return render(request, 'main/students.html', {'students': studentdata})