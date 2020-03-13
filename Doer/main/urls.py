from django.urls import path
from django.contrib.auth.views import LoginView
from . import views,forms

app_name = 'main'
urlpatterns = [
    path('',views.index,name="home"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('login/',LoginView.as_view(template_name='main/login.html',form_class=forms.LoginForm),name='login'),
    path('logout/',views.logout_view,name="logout"),
    path('main/',views.MainView.as_view(),name="main"),
    path('main/add-task/',views.add_task,name="add_task"),
]