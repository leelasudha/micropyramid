from django.shortcuts import render,redirect
from .models import Employee
from django.http import HttpResponse
# Create your views here.
def register(request):
	if request.method == "POST":
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		obj = Employee(fname= fname, lname=lname, email= email, mobile=mobile)
		obj.save()
		return HttpResponse('Employee added successfuly')
	return render(request, 'employee/register.html')

def show(request):
	data = Employee.objects.all()
	return render(request, 'employee/show.html',{'data':data})

def edit(request, id):
	data = Employee.objects.get(id = id)
	if(request.method =="POST"):
		data.fname = request.POST.get('fname')
		data.lname = request.POST.get('lname')
		data.email = request.POST.get('email')
		data.mobile = request.POST.get('mobile')
		data.save()
		return redirect('show')
	return render(request, 'employee/edit.html', {'data':data})
def delete(request, id):
	data = Employee.objects.get(id = id)
	data.delete()
	return HttpResponse('Employee deleted successfuly')


