"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render,redirect
from my_app import views
from django.conf.urls import url
from django.urls import re_path
from my_app import models
def my_test_login_def(request):
    '''
    处理用户请求，并返回内容
    :param request: 用户请求相关所有信息
    :return:
    '''

    if request.method == "GET":
        #return HttpResponse('login')   # HttpResponse 只加字符串
        return render(request,'my_test_login.html')   #自动找到模板路径下的html文件，读取内容并返回给用户
    else:
         #用户post提交的数据
         u = request.POST.get('user')
         p = request.POST.get('pwd')
         if u == 'root' and p =='123123':
             #return redirect('http://www.oldboyedu.com')   返回一个已成熟的运行网站
             return redirect('/index/')
         else:
             '''登录失败'''
             return render(request,'my_test_login.html',{'msg':'用户名或密码错误'})



def login(request):
    return render(request,'login.html')


def test007(request):
    return render(request,'test007.html')
def test008(request):
    return render(request,'test008.html')



urlpatterns = [
    #path('admin/', admin.site.urls),

    path('my_test_login/', my_test_login_def),   #测试启动我的第一个页面 ，后面的代表函数名

    path('test007/', test007),
    path('test008/', test008),

    path('login/', login),
    path('',views.to_login),     #保证一打开端口即显示固定的页面


    path('check_login/', views.check_login),
    path('check_register/', views.check_register),     #这些链接响应action,用以处理post提交的form表单
    path('change_pass/', views.change_pass),        #前一个为html中的请求路径，html根据请求路径请求到达这里，然后到views中查找相关的方法
    path('problem/', views.problem),
    path('ans_ajax/',views.ans_ajax),

    path('index_01/', views.index_01, name="index_01"),


    path('to_register/', views.to_register, name="to_register"),     #这些path只是实现简单的页面跳转
    path('to_login/', views.to_login, name="to_login"),
    path('index_02/', views.index_02, name="index_02"),
    path('index_02_01/', views.index_02_01, name="index_02_01"),
    path('index_02_02/', views.index_02_02, name="index_02_02"),
    path('index_02_03/', views.index_02_03, name="index_02_03"),
    path('homepage/', views.homepage, name="homepage"),
    path('index_05_01/', views.index_05_01, name="index_05_01"),
    path('index_05_02/', views.index_05_02, name="index_05_02"),
    path('index_07/', views.index_07, name="index_07"),
    path('index_03/', views.index_03, name="index_03"),
    path('index_03_01/', views.index_03_01, name="index_03_01"),
    path('index_04/', views.index_04, name="index_04"),







    path('index_06/', views.index_06, name="index_06"),          #此链接跳转至正常运行的成熟网站
]
