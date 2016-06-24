from django.shortcuts import render, get_object_or_404
from .models import info_client
from .forms import info_client_Form
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'seoulcrawl/home.html',{})

def join(request):
    if  request.method =="POST":
        form = info_client_Form(request.POST)
        if form.is_valid():
            #firstname = form.cleaned_data['firstname']
            #lastname = form.cleaned_data['lastname']
            #email = form.cleaned_data['email']
            #join_date = form.cleaned_data['join_date']
            #text = form.cleaned_data['text']
            post = form.save()
            return redirect('seoulcrawl.views.home')
    else:
        form = info_client_Form()    
    return render(request, 'seoulcrawl/join.html',{'form':form})
def register(request):
    """signup
    to register users
    """
    if request.method =="post":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()
            
            return HttpResponseRedirect(
                reverse("register_ok")
            )
    elif request.method =="GET": #만약 GET방식이라면
    # UserCreationForm 클래스를 이용해 userform이라는 객체를 만들어라
        userform = UserCreationForm()
    return render(request, "seoulcrawl/register.html",{
        "userform":userform,
    })

def register_ok(request):
    return render(request, 'seoulcrawl/register_ok.html',{})    


    
# def register(request):
#    if request.method =='POST':#가입신청서가 날아오면 발동, 문제 없으면 (is_valid)USER모델에 저장(create_user)
#        form = RegistrationForm(request.POST)
#    if form.is_valid():
#        user = User.objects.create_user(
#            username = form.cleaned_data['username'],
#            password = form.cleaned_data['password'],           
#        ) 
#        return HttpResponseRedirect
#    else : #그외경우 form 깔끔히 청소
#        form = RegistrationForm()
#    return render(request, 'register.html',{'form':form}) # 가입 신청서를 내지 않았거나 장못된 신청서
    