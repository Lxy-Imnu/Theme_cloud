from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from theme_cloud import models


def index(request):
    return render(request, 'index.html')


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        cpassword = request.POST.get('cpwd')
        code = request.POST.get('code')
        if not all([username, password, cpassword]):
            # 数据不完整
            return render(request, 'index.html', {'errmsg': '数据不完整'})
        # 校验用户名是否重复
        try:
            user = models.User.objects.get(name=username)
        except models.User.DoesNotExist:
            # 用户名不存在
            user = None
        if user:
            # 用户名已存在
            return render(request, 'register.html', {'errmsg': '用户名已存在'})
        if not all([username, password, cpassword]):
            return render(request, 'register.html', {'errmsg': '请完善数据'})
        '''if code != code.captcha:
            return render(request, 'register.html', {'errmsg': '验证码错误'})'''
        user = models.User.objects.create()
        user.name = username
        mpassword = make_password(password, None, 'pbkdf2_sha256')
        user.password = mpassword
        user.save()
        return render(request, 'register_success.html')

def register_success(request):
    return render(request, 'register_success.html')


def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'login/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'register_success.html', locals())


# 登录
def login_views(request):
    if request.session.get('is_login', None):
        return redirect("/index/")

    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
                # 密码解密验证
                pwd_bool = check_password(password, user.password)
            except:
                message = "用户不存在！"

            if pwd_bool == True:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return JsonResponse({'res': 1})
            else:
                return JsonResponse({'res': 0})
        else:
            return render(request, 'login.html', {'errmsg': '请完善数据'})


def logout_views(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")


# 关于我们
def about(request):
    return render(request, 'about.html')


# 主题词云使用说明书
def instruction(request):
    return render(request, 'instruction.html')


# 制作词云
def work(request):
    return render(request, 'work.html')


# 联系我们
def contact(request):
    return render(request, 'contact.html')
