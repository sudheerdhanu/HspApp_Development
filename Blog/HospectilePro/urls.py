"""HospectilePro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import sys
sys.path.append(".")
from django.contrib import admin
from django.urls import path,include
# from Blog.HspApp.Views import security
from HspApp.Views import security
from HspApp.Views import home
from HspApp.Views import sms


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/', security.sign_up ,name='sign_up'),
    path('home/', home.home_page ,name='home_page'),
    # path('', include('django.contrib.auth.urls')),
    path("login/", security.login1, name="login"),
    path("send/", sms.send, name="send"),


]
