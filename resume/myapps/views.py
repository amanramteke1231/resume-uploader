from django import views
from django.shortcuts import render
from requests import request
from .forms import Resumeform
from .models import Resume
from django.views import View
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

class HomeView(View):
    def get(self, request):
        form = Resumeform()
        candidates = Resume.objects.all()
        paras = {'form': form,
                 'candidates':candidates}
        return render(request, "myapp/home.html",paras)
    
    def post(self, request):
        form = Resumeform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        try:
            return HttpResponseRedirect('/')
        except:
            return render(request, "myapp/home.html", {'form':form})

class CandidateView(View):
    def get(self,request,cd):
        candid = Resume.objects.get(cd=cd)
        a = {
            'candid': candid
        }
        return render(request, 'myapp/candidate.html', a)
    