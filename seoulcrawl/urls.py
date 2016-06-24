from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.home, name = 'home'),
    url(r'^join/$',views.join, name = 'join'),
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        name = 'login_url',
        kwargs = {
            'template_name' : 'login.html'
        }
     ),
    url(
         r'^logout/$',
         'django.contrib.auth.views.logout',
         name = 'logout_url'
     ),
    url(r'^register/$',views.register, name ='register'),
    url(r'^register_ok/$', TemplateView.as_view(
        template_name ='seoulcrawl/register_ok.html'
        ), name = 'register_ok'),  
]

urlpatterns +=static('static_files',document_root = settings.MEDIA_ROOT)