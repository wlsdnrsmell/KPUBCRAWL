from django.shortcuts import render, get_object_or_404
from .models import info_client
from .forms import info_client_Form
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'seoulcrawl/home.html',{})

def join(request):
    if  request.method =="POST":
        form = info_client_Form(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('seoulcrawl.views.home')
    else:
        form = info_client_Form()    
    return render(request, 'seoulcrawl/join.html',{'form':form})