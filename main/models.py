from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    branch = models.CharField(max_length=10)
    year = models.IntegerField()
    section = models.CharField(max_length=1)
    gender = models.CharField(max_length=1)

    date_of_birth = models.DateField()
    date_of_joining = models.DateField()

    cgpa = models.FloatField()
    attendance = models.FloatField()

    is_active = models.BooleanField(default=True)
    scholarship = models.BooleanField(default=False)

    address = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name