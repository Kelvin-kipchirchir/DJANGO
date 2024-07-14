from django.db import models

# Create your models here.
class Careers(models.Model):
	career = models.CharField(max_length=200)
	description = models.TextField(null=True,blank=True)

	def __str__(self):
		return self.career

class Education(models.Model):
	level = models.CharField(max_length=50)
	course = models.CharField(max_length=200)
	institution = models.CharField(max_length=200)
	avatar = models.ImageField(null=True, default="avatar.svg")
	year_started = models.DateField()
	year_completed = models.DateField()

	class Meta:
		ordering = ['year_completed']

	def __str__(self):
		return self.course

class Experience(models.Model):
	role = models.CharField(max_length=50)
	company = models.CharField(max_length=200)
	avatar = models.ImageField(null=True, default="avatar.svg")
	city = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	year_started = models.DateField()
	year_completed = models.DateField()
	#duties = models.TextField()

	class Meta:
		ordering = ['year_completed']

	def __str__(self):
		return self.role

class Skill(models.Model):
	skill_type = models.CharField(max_length=50)
	name = models.CharField(max_length=50)

	def __str_(self):
		return self.name

class Project(models.Model):
	project_type = models.CharField(max_length=100)
	project_name = models.CharField(max_length=100)
	project_client = models.CharField(max_length=100)
	avatar = models.ImageField(null=True, default="avatar.svg")
	project_date = models.DateField()
	project_url = models.CharField(max_length=100)
	project_photos = models.ImageField()
	project_details = models.TextField()

	class Meta:
		ordering = ['project_date']

	def __str__(self):
		return self.project_name

