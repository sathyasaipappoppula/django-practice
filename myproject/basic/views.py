from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import math
import json
from django.views.decorators.csrf import csrf_exempt 
from basic.models import userProfile,Employee 
from django.db.utils import IntegrityError

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')
def sample1(request):
    q1=request.GET.get("name")
    q2=request.GET.get("city")
    return HttpResponse(f"{q1} came from {q2}")


def StudentsByCity(request):
    students_data=[{'name':'durgaprasad','city':'hyd'},{'name':'sai','city':'hyd'},{'name':'uma','city':'bnglr'},{'name':'kiran','city':'bnglr'}]
    filteredStudents=[]
    city=request.GET.get("city","hyd")
    for student in students_data:
        if student["city"]==city:
            filteredStudents.append(student)
            
    return JsonResponse({"status":"success","data":filteredStudents})


def arraySlicing(request):
    data=['apple','banana','carrot','grapes','watermelon','kiwi','pineapple','custard-apple','strawberry','blueberry','dragonfruit']
    page=int(request.GET.get('page',1))
    limit=int(request.GET.get('limit',3))
    start=(page-1)*limit
    end=page*limit
    output=data[start:end] 
    return JsonResponse({"data":output})

@csrf_exempt
def createData(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body) #dictionary
            name=data.get("name") #taking name property from dict
            age=data.get("age") #taking age property from dict
            city=data.get("city") #taking city property from dict
            userProfile.objects.create(name=name,age=age,city=city)
            print(data)
        return JsonResponse({"status":"success","data":data,"statuscode":201},status=201)
    except Exception as e:
        return JsonResponse({"statuscode":500,"message":"internal server error"})

@csrf_exempt
def createProduct(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
    return JsonResponse({"status":"success","data":data,"statuscode":201})
@csrf_exempt
def createEmployee(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            print(data)
            Employee.objects.create(emp_name=data.get("name"),emp_salary=data.get("sal"),emp_email=data.get("email"))
        return JsonResponse({"status":"success","data":data,"statuscode":201},status=201)
    except IntegrityError as e:        
        return JsonResponse({"status":"error","message":"inputs are invalid or not acceptable"},status=400)
    finally:
        print("done")

