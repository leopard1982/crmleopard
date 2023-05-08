from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime

from django.conf import settings

from django.contrib.auth.models import User

from .forms import SignUpForm

from django.contrib.auth.decorators import login_required

from .forms_buatan import InputRecord, UpdateRecord

from .models import Record

from django.core.paginator import Paginator


# Create your views here.
def welcome(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']

		#authenteciated
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			messages.success(request,"You have been loged in!")
			return redirect('welcome')
		else:
			messages.success(request,"Username or Password Different! Please Try Again!")
			return redirect('welcome')
	else:
		return render(request,'welcome.html')

def user_login(request):
	return HttpResponse("login")

def user_logout(request):
	logout(request)
	messages.success(request,"You Have Been Logout!")
	return HttpResponseRedirect("/")

def error_404(request,exception):
	return render(request,'error404.html')

def error_500(request,exception=None):
	return render(request,'error404.html')


def register_user(request):
	if request.method=="POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			users = User.objects.all()
			if users.count()<settings.MAX_USER:
				form.save()
				messages.success(request,"User Successfully Created! Please Login to Continue!")
			else:
				messages.success(request,"For Trial Version Just Create %s User! Please Contact Vendor!"%settings.MAX_USER)
			return redirect('welcome')
		else:
			messages.success(request,"Error Create User! Please Try Again!")
			return render(request,'register.html',{'signupform':form})
	else:
		_signupform = SignUpForm()
		return render(request,'register.html',{'signupform':_signupform})

@login_required(login_url="/")
def add_record(request):
	if request.method=="POST":
		forms = InputRecord(request.POST)
		if(forms.is_valid()):
			forms.save()
			messages.success(request,"Great! Record Has Been Successfully Added!")
			return redirect('add_record')
		else:
			messages.success(request,"Upss.. Error in Added Record! Please Try Again")
			print(forms)
			return redirect('add_record')
	else:
		data = {
			'first_name':' ',
			'last_name' : ' ',
			'address' : ' ',
			'city' : ' ',
			'state' : ' ',
			'province':' ', 
			'kode_pos':' ',
			'email' : ' ',
			'phone': ' ',
			'created_by': request.user.username
		}
		forms = InputRecord(data)
		return render(request,'inputRecord.html',{'forms':forms})

@login_required(login_url="/")
def view_record(request):
	# if request.method=="POST":
	# 	datas = Record.objects.all().filter(first_name="")
	# 	forms = UpdateRecord(request.POST)
	# 	if(forms.is_valid()):
	# 		forms.save()
	# 		messages.success(request,"Great! Record Has Been Successfully Added!")
	# 		return redirect('add_record')
	# 	else:
	# 		messages.success(request,"Upss.. Error in Added Record! Please Try Again")
	# 		return redirect('add_record')
	# else:
	# 	forms = InputRecord()
	# 	return render(request,'inputRecord.html',{'forms':forms})
	data = Record.objects.all()
	p = Paginator(data,5)
	try:
		myp= p.get_page(request.GET.get('page'))
	except:
		myp= p.get_page(1)
	return render(request,'daftar.html',{'data':myp})


@login_required(login_url="/")
def view_detail(request,pk):
	# if request.method=="POST":
	# 	datas = Record.objects.all().filter(first_name="")
	# 	forms = UpdateRecord(request.POST)
	# 	if(forms.is_valid()):
	# 		forms.save()
	# 		messages.success(request,"Great! Record Has Been Successfully Added!")
	# 		return redirect('add_record')
	# 	else:
	# 		messages.success(request,"Upss.. Error in Added Record! Please Try Again")
	# 		return redirect('add_record')
	# else:
	# 	forms = InputRecord()
	# 	return render(request,'inputRecord.html',{'forms':forms})

	try:
		if(int(pk)==0):
			data = Record.objects.get(id=1)
		else: 
			data = Record.objects.get(id=pk)
		
	except:
		data = Record.objects.all().order_by("-id")
		data= Record.objects.get(id=data[0].id)
	return render(request,'detailclient.html',{'data':data})

def testunit(request):
	return HttpResponse(request.GET.get('nama'))

