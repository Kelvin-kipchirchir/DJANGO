
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Careers,Education,Experience,Skill,Project
from .forms import ProjectForm,EducationForm


# Create your views here.

profilepic = [
{'id':1,'pic':'my pic'}
]
abouts = [
{'id':1,'bio':'hello am kelvin kipchirchir a proffessional cyber Security enginner This is kelvin kipchirchir a developer,Security Analyst,A hacker'},
]

personalinfo = [
{'id':1,'pinfo':'website','role':'www.kevoempire.com'},
{'id':2,'pinfo':'phoneno','role':'0795711976'},
{'id':3,'pinfo':'city','role':'Nairobi,Kenya'}
]


def home(request):
	careers = Careers.objects.all()
	education = Education.objects.all()
	experience = Experience.objects.all()
	skills = Skill.objects.all()
	projects = Project.objects.all()
	context = {'abouts':abouts,'careers':careers,'profilepic':profilepic,
	'personalinfo':personalinfo,'skills': skills,'education':education,'experience':experience,'projects':projects}
	return render(request,"base/home.html",context)

def skill(request,pk):
	skill = None
	for i in skills:
		if i['id'] == int(pk):
			skill = i
	context = {'skill': skill}
	return render(request,"base/skill.html",context)

def aboutPage(request):
	careers = Careers.objects.all()
	context = {'abouts':abouts,'careers':careers,'profilepic':profilepic,'personalinfo':personalinfo,'skills': skills}
	return render(request,"base/about.html",context)

def dashboardPage(request):
	return render(request,"base/dashboard.html")

def loginPage(request):
	careers = Careers.objects.all()
	education = Education.objects.all()
	experience = Experience.objects.all()
	skills = Skill.objects.all()
	projects = Project.objects.all()
	context = {'abouts':abouts,'careers':careers,'profilepic':profilepic,
	'personalinfo':personalinfo,'skills': skills,'education':education,'experience':experience,'projects':projects}
	return render(request,"base/dashboard.html",context)

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"base/dashboard.html",{'form': form})
def addEducation(request):
	form = EducationForm()
	if request.method == 'POST':
		form = EducationForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	context = {'form':form}		
	return render(request,"base/add_education.html",{'form':form})

def updateEducation(request,pk):
	education = Education.objects.get(id=pk)
	form = EducationForm(instance=education)
	if request.method == 'POST':
		education.level = request.POST.get('level')
		education.course = request.POST.get('course')
		education.institution = request.POST.get('institution')
		education.avatar = request.POST.get('avatar')
		education.year_started = request.POST.get('year_started')
		education.year_completed = request.POST.get('year_completed')
		education.save()
		return redirect('login')
	return render(request,"base/add_education.html",{'form':form})
	

