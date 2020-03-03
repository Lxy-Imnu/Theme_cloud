import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'projectname.settings'

if __name__ == '__main__':

    send_mail(
        '来自www.xxxxx.com的测试邮件',
        '欢迎访问www.xxxxx.com，这里是xx站点，本站专注于xx内容的分享！',
        'xxx@qq.com',
        ['xxx@qq.com'],
    )



#HTML格式邮件
import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自www.xxxxx.com的测试邮件', 'xxx@qq.com', 'xxx@qq.com'
    text_content = '欢迎访问www.xxxxx.com，这里是xx站点，专注于xx技术的分享！'
    html_content = '<p>欢迎访问<a href="http://www.baidu.com" target=blank>www.xxx.com</a>，这里是xx的站点，专注于xx技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()