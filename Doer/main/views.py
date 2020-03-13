from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout
from . import forms, models
from datetime import date
import calendar

# Create your views here.
def index(req):
    return render(req,'main/index.html')

class SignUpView(FormView):
    form_class = forms.UserCreationForm
    success_url = '/main/'
    template_name = 'main/signup.html'

    def form_valid(self,form):
        response = super().form_valid(form)

        form.save()

        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')

        user = authenticate(self.request,username=username,password=raw_password)

        login(self.request,user)

        return response

class MainView(LoginRequiredMixin,TemplateView):
    template_name = "main/main.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()
        cal = calendar.Calendar()

        tasks = models.Task.objects.filter(user = self.request.user)
        #months = ["January","February","March"]
        
        context['today'] = today
        context['weeks'] = cal.monthdatescalendar(today.year,today.month)
        context['tasks'] = tasks

        return context

def logout_view(req):
    if req.method == "POST":
        logout(req)
        return redirect(reverse('main:home'))
    else:
        return render(reverse('main:home'))

def add_task(req):
    if req.method == "POST" and req.user.is_authenticated:
        description = req.POST.get('description')
        task = models.Task(description = description, user = req.user)
        task.save()
        return redirect('main:main')