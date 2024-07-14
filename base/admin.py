from django.contrib import admin

# Register your models here.
from .models import Careers,Education,Experience,Skill,Project

admin.site.register(Careers)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Project)

