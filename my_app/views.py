from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import HttpResponse,render,redirect
from django.views.decorators.csrf import csrf_exempt

from my_app import models


def check_login(request):
    if request.method == "POST":
        username = request.POST.get('userName', None)
        password = request.POST.get('passWord', None)
        message = "所有字段都必须填写！"
        #if username =='admin' and password =='123456':///此处试验成功，成功从表单处得到输入的用户名和密码
        #    return redirect('homepage')
        #else:
        #    return render(request, 'register.html')
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    models.User.objects.filter(name=username).update(login_num=user.login_num+1)     #登录成功，则表中字段login_num+1,表示登录次数加一
                    user_name = user.name
                    request.session['user_name'] = user_name
                    user_id = user.id
                    request.session['user_id'] = user_id
                    total_login = user.login_num
                    request.session['total_login'] = total_login
                    total_users_num = models.User.objects.count()
                    request.session['total_users_num'] = total_users_num
                    request.session['password'] = user.password
                    return render(request, 'homepage.html', {"user_name": user_name,"user_id":user_id,"total_login":total_login,"total_users_num":total_users_num})
                else:
                     message = "密码不正确！"
            except:
                     message = "用户名不存在！"
        return render(request, 'login.html', {"message": message})
    return render(request, 'login.html')


def check_register(request):
    if request.method == "POST":
        username = request.POST.get('registerUsername', None)
        password = request.POST.get('registerPasswords', None)
        check_pass = request.POST.get('registerPassword', None)
        message = "所有字段都必须填写！"
        #if username =='admin' and password =='123456':       #此处试验成功，成功从表单处得到注册的用户名和密码
        #    return redirect('homepage')
        #else:
        #    return render(request, 'register.html')
        if password != check_pass:
            message = "添加失败，请保持密码一致！"
            return render(request, 'register.html', {"message": message})
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                message = "用户已存在！"
                return render(request, 'register.html', {"message": message})
            except:
                num = models.User.objects.count() + 1
                models.User.objects.create(id=num, name=username, password=password, login_num=0)
                message = "用户创建成功！"
                return render(request, 'login.html', {"message": message})
    return render(request, 'register.html')

def change_pass(request):
    if request.method == "POST":
        oldpass = request.POST.get('oldpass', None)
        newpass = request.POST.get('newpass', None)
        renewpass = request.POST.get('renewpass', None)
        password = request.session.get('password', default='')
        user_name = request.session.get('user_name', default='')
        user_id = request.session.get('user_id', default='')
        total_login = request.session.get('total_login', default='')
        total_users_num = request.session.get('total_users_num', default='')
        message = "修改成功！"
        #if oldpass =='admin' and newpass =='123456' and renewpass == '123456':       #此处试验成功，成功从表单处得到新旧密码
        #    return redirect('homepage')
        #if password == '123456':                        #此处试验成功，成功获得session中存储的正确旧密码
        #    return redirect('homepage')
        #else:
        #    return render(request, 'register.html')
        if oldpass == password:
            if newpass == renewpass:
                models.User.objects.filter(id=user_id).update(password=newpass)
                return render(request, 'login.html', {"message": message})
            else:
                message = "修改密码失败：两次输入的新密码不一致！"
                return render(request, 'index_04.html', {"message": message,"user_name":user_name,"user_id":user_id,"total_login":total_login,"total_users_num":total_users_num})
        else:
            message = "修改密码失败：旧密码输入错误！"
            return render(request, 'index_04.html', {"message": message,"user_name":user_name,"user_id":user_id,"total_login":total_login,"total_users_num":total_users_num})

def index_03(request):
    user_name = request.session.get('user_name', default='')
    user_id = request.session.get('user_id', default='')
    return render(request, 'index_03.html',{"user_name":user_name,"user_id":user_id})


def problem(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        subject = request.POST.get('subject', None)
        message = request.POST.get('message', None)
        user_name = request.session.get('user_name', default='')
        user_id = request.session.get('user_id', default='')
        #if user_name =='admin':       #此处试验成功，成功从表单处得到输入的数据，并从session处得到封装的用户名以及id
        #    return redirect('homepage')
        #else:
        #    return render(request, 'register.html')
        num = models.Pro.objects.count() + 1
        models.Pro.objects.create(pro_id=num,user_id=user_id, user_name=user_name,mail=email,theme=subject,content=message)

        problems = models.Pro.objects.all()  #Queryset
        return render(request, 'index_03_01.html',{"problems":problems})


def index_03_01(request):
    problems = models.Pro.objects.all()  # Queryset
    ans = models.Ans.objects.all()
    user_name = request.session.get('user_name', default='')
    return render(request,'index_03_01.html',{"problems":problems,"user_name":user_name,"ans":ans})

def index_04(request):
    user_name = request.session.get('user_name',default='')
    user_id = request.session.get('user_id', default='')
    total_login = request.session.get('total_login', default='')
    total_users_num = request.session.get('total_users_num', default='')
    password = request.session.get('password', default='')
    return render(request, 'index_04.html',{"user_name":user_name,"user_id":user_id,"total_login":total_login,"total_users_num":total_users_num,"password":password})

@csrf_exempt
def ans_ajax(request):
    text = request.POST.get('text',None)
    pro_id = request.POST.get('pro_id', None)
    #if pro_id == "1":                                #此处试验成功，成功获得post传递的参数text   成功获取字符串pro_id
    #    return redirect('homepage')
    #else:
    #    return render(request, 'register.html')
    user_name = request.session.get('user_name', default='')
    num = models.Ans.objects.count() + 1
    models.Ans.objects.create(ans_id=num,ans_content=text,to_pro_id=pro_id,user_name=user_name)      #成功创建了
    problems = models.Pro.objects.all()  # Queryset
    ans = models.Ans.objects.all()
    return render(request, 'index_03_01.html', {"problems": problems, "user_name": user_name, "ans": ans})


def index_01(request):
    return render(request, 'index_01.html')


def homepage(request):
    return render(request, 'homepage.html')
def to_register(request):
    return render(request, 'register.html')
def to_login(request):
    return render(request, 'login.html')
def index_02(request):
    return render(request, 'index_02.html')
def index_02_01(request):
    return render(request, 'index_02_01.html')
def index_02_02(request):
    return render(request, 'index_02_02.html')
def index_02_03(request):
    return render(request, 'index_02_03.html')
def index_05_01(request):
    return render(request, 'index_05_01.html')
def index_05_02(request):
    return render(request, 'index_05_02.html')
def index_07(request):
    return render(request, 'index_07.html')
def index_06(request):
    return redirect('https://blog.csdn.net/qq_38175040/article/details/105555979')









