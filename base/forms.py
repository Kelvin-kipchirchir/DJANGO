from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Project,Education


class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['project_type','project_name','project_client','avatar',
		'project_date','project_url','project_photos','project_details']



class EducationForm(ModelForm):
	class Meta:
		model = Education
		fields = '__all__'
		