from django.shortcuts import render,redirect
from Employee.models import EMP_DETAILS

# Create your views here.
def home(request):
    if (request.method=='POST'):
        first_=request.POST['first']
        last_=request.POST['last']
        salary_=request.POST['salary']
        address_=request.POST['address']
        email_=request.POST['email']
        password_=request.POST['password']
        print(first_)

        insert_data=EMP_DETAILS.objects.create(first_name=first_,last_name=last_,salary=salary_,address=address_,email=email_,password=password_,)
        insert_data.save()
        return redirect('/')
    return render(request,'Employee/home.html')


def empdet(request):
    content={}
    content['data']=EMP_DETAILS.objects.filter(is_deleted='no')
    return render(request,'Employee/empdet.html',content)


def delete(request,tid):
    record_to_delete=EMP_DETAILS.objects.filter(id=tid)
    record_to_delete.update(is_deleted="y")
    return redirect('/')

def update(request,tid):
    if (request.method=='POST'):
        first_=request.POST['first']
        last_=request.POST['last']
        salary_=request.POST['salary']
        address_=request.POST['address']
        email_=request.POST['email']
        password_=request.POST['password']
        record_to_update=EMP_DETAILS.objects.filter(id=tid)
        record_to_update.update(first_name=first_,last_name=last_,salary=salary_,address=address_,email=email_,password=password_)
        return redirect('/')
    else:
        content={}
        content['data']=EMP_DETAILS.objects.get(id=tid)
        return render(request,'Employee/update.html',content)
