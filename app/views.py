from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib.auth import authenticate
from datetime import datetime
from Theme import settings
from app import models
from app.models import User


# Create your views here.
# class RegisterView(View):
#     def get(self, request):
#         return render(request, 'index.html')
#
#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         cpassword = request.POST.get('cpwd')
#         email = request.POST.get('email')
#         # 校验用户名是否重复
#         if not all([username, password, cpassword, email]):
#             return JsonResponse({'res': 2})
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             # 用户名不存在
#             user = None
#         if user:
#             # 用户名已存在
#             return JsonResponse({'res': 0})
#         user = User.objects.create_user(username, email, password)
#         # user.is_active = 0
#         user.save()
#         return JsonResponse({'res': 1})


def index(request):
    return render(request, 'index.html')


@csrf_exempt
# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpwd')
        email = request.POST.get('email')
        # 校验用户名是否重复
        if not all([username, password, cpassword, email]):
            return JsonResponse({'res': 2})
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None
        if user:
            # 用户名已存在
            return JsonResponse({'res': 0})
        user = User.objects.create_user(username, email, password)
        # user.is_active = 0
        user.save()
        return JsonResponse({'res': 1})


def register_success(request):
    return render(request, 'register_success.html')


# 邮箱验证
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
        return render(request, 'index.html', locals())


# 登录
# josn数据
# {'res': 0}# 用户名或密码错误
# {'res': 1}# 登录成功
# {'res': 2}# 数据不完整
# {'res': 3}# 用户未激活
@csrf_exempt
def login_views(request):
    if request.session.get('is_login', None):
        return redirect("/index/")

    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        code = request.POST.get('code')
        if not all([username, password]):
            return JsonResponse({'res': 2})  # 数据不完整
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session['is_login'] = True
                request.session['user_name'] = username
                login(request, user)
                return JsonResponse({'res': 1})  # 登录成功
            else:
                return JsonResponse({'res': 3})  # 用户未激活
        else:
            return JsonResponse({'res': 0})  # 用户名或密码错误


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
    if request.method == 'POST':
        user = request.POST.get('')
        email = request.POST.get('')
        summary = request.POST.get('')
        message = request.POST.get('')
        time = datetime.now()

    return render(request, 'contact.html')
