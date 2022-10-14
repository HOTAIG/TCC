from django.shortcuts import render, redirect
from StudioApp.forms import UsersForm
# Create your views here.

def home(request):
	return render(request,'index.html',{})

def cadastro(request):
	data = {}
	data['form'] = UsersForm()
	return render(request,'cadastro.html',data)

def docad(request):
	form = UsersForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('cadastro')

