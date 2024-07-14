from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name="home"),
path('skill/<str:pk>/',views.skill,name="skill"),
path('about/',views.aboutPage,name="about"),
path('login/',views.loginPage,name="login"),
path('dashboard/',views.dashboardPage,name="dashboard"),
path('add-education/',views.addEducation,name="add-education"),
path('update-education<str:pk>/',views.updateEducation,name="update-education"),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)