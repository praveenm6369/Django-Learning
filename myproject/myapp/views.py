from django.shortcuts import render
from .models import Emp

# Create your views here.
def home(request):
    return render(request,"home.html")

employee=Emp(
    name="praveen",
    age=21,
    email="praveen@gmail.com",
    salary=20000,
    place="coimbatore"
)

employee.save()


