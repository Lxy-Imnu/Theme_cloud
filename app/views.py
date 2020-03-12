from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

from django.views import View
from Theme import settings
from app import models
from app.models import User
from django.core.mail import send_mail
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from django.conf import settings


# Create your views here.

# 主页
def index(request):
    return render(request, 'index.html')


# 注册成功反馈页面
def register_success(request):
    return render(request, 'register_success.html')


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
#         user.is_active = 0
#         user.save()
#         # 发送用户的激活邮件，包含激活链接：http://127.0.0.1:8000/user_active/id
#         # 激活链接中要包含用户的身份信息，并且把身份信息加密
#         # 加密用户的身份信息，生成激活的token
#         serializer = Serializer(settings.SECRET_KEY, 7200)
#         info = {'confirm': user.id}
#         token = serializer.dumps(info)
#         token = token.decode()
#         # 发邮件
#         subject = '主题词云欢迎您'
#         message = ''
#         sender = settings.EMAIL_FROM
#         recipient = [email, sender]
#         html_massage = '<h1>%s，欢迎您成为主题词云注册用户</h1>请点击下面链接激活您的账户<br/><a href="http://127.0.0.1:8000/user_active/%s" target=blank>http://127.0.0.1:8000/user_active/%s</a>' % (
#             username, token, token)
#         send_mail(subject, message, sender, recipient, html_message=html_massage)
#         return JsonResponse({'res': 1})


# class ActiveView(View):
#     def get(self, request, token):
#         serializer = Serializer(settings.SECRET_KEY, 7200)
#         try:
#             serializer.loads(token)
#             info = serializer
#             user_id = info['confirm']
#             user = User.objects.get(id=user_id)
#             user.is_active = 1
#             user.save()
#             return render(request, 'index.html')
#         except SignatureExpired as e:
#             return HttpResponse('该激活链接已过期')


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
        user.is_active = 0
        user.save()
        # 发送用户的激活邮件，包含激活链接：http://127.0.0.1:8000/user_active/id
        # 激活链接中要包含用户的身份信息，并且把身份信息加密
        # 加密用户的身份信息，生成激活的token
        serializer = Serializer(settings.SECRET_KEY, 7200)
        info = {'confirm': user.id}
        token = serializer.dumps(info)
        token = token.decode()
        # 发邮件
        subject = '主题词云欢迎您'
        message = ''
        sender = settings.EMAIL_FROM
        recipient = [email, sender]
        html_massage = '<h1>%s，欢迎您成为主题词云注册用户</h1>请点击下面链接激活您的账户<br/><a href="http://127.0.0.1:8000/user_active/%s" target=blank>http://127.0.0.1:8000/user_active/%s</a>' % (
            username, token, token)
        send_mail(subject, message, sender, recipient, html_message=html_massage)
        return JsonResponse({'res': 1})


# 用户激活
def user_active(request, token):
    if request.method == 'GET':
        serializer = Serializer(settings.SECRET_KEY, 7200)
        try:
            serializer.loads(token)
            info = serializer
            user_id = info['confirm']
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()
            return render(request, 'index.html')
        except SignatureExpired as e:
            return HttpResponse('该激活链接已过期')


# 登录
# josn数据
# {'res': 0}# 用户名或密码错误
# {'res': 1}# 登录成功
# {'res': 2}# 数据不完整
# {'res': 3}# 用户未激活

# class LoginView(View):
#     def get(self, request):
#         return render(request, 'index.html')
#
#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         code = request.POST.get('code')
#         if not all([username, password, code]):
#             return JsonResponse({'res': 2})  # 数据不完整
#         # if code != code:
#         #     return JsonResponse({'res': 4})
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user and user.is_active:
#                 login(request, user)
#                 request.session['is_login'] = True
#                 request.session['user_name'] = username
#                 return JsonResponse({'res': 1})  # 登录成功
#             else:
#                 return JsonResponse({'res': 3})  # 用户未激活
#         else:
#             return JsonResponse({'res': 0})  # 用户名或密码错误

# verify_code
def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 30
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    # font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体对象，windows的字体路径
    font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def login_views(request):
    if request.session.get('is_login', None):
        return redirect("/index/")

    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        code = request.POST.get('code')
        if not all([username, password, code]):
            return JsonResponse({'res': 2})  # 数据不完整
        if code != request.session.get('verifycode'):
            return JsonResponse({'res': 4})
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['is_login'] = True
                request.session['user_name'] = username
                return JsonResponse({'res': 1})  # 登录成功
            else:
                return JsonResponse({'res': 3})  # 用户未激活
        else:
            return JsonResponse({'res': 111111})  # 用户名或密码错误


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
    if request.method == 'GET':
        return render(request, 'contact.html')

    if request.method == 'POST':
        msg = models.Message()
        msg.name = request.POST.get('name')
        msg.email = request.POST.get('eml')
        msg.summary = request.POST.get('subject')
        msg.message = request.POST.get('message')
        msg.save()
        subject = '系统收到一封建议'
        message = ''
        sender = settings.EMAIL_FROM
        recipient = [msg.email]
        html_massage = '<h1>%s，为系统发了一封建议</h1><br/><h2>%s<h2><br/><p>%s</p><br>From: $email%s' % (
        msg.name, msg.summary, msg.message, msg.email)
        send_mail(subject, message, sender, recipient, html_message=html_massage)
        return JsonResponse({'res': 1})
