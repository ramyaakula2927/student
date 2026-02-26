from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')


def colleges(request):
    collegelist = ['SVECW', 'VIT', 'BVRICE']
    
    return render(request, 'colleges.html', {'colleges': collegelist})


studentdata = [
    {'rno': 1201, 'name': 'Harinya', 'age': 21, 'branch': 'CSE'},
    {'rno': 1202, 'name': 'Madhu', 'age': 17, 'branch': 'ECE'},
    {'rno': 1203, 'name': 'Hamsa', 'age': 21, 'branch': 'MECH'},
]


def student(request):   # function name should be lowercase
    return render(request, 'main/students.html', {'students': studentdata})