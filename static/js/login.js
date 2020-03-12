//点击登录按钮 ，提交数据
jQuery(document).ajaxSend(function (event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});


function login() {
    let username = document.getElementById("l_username").value;
    let password = document.getElementById("l_pwd").value;
    let code = document.getElementById("code").value;

    $.ajax({
        'url': '/login/',
        'dataType': 'json',
        'type': 'post',
        'data': {
            'username': username,
            'password': password,
            'code': code
        },
        success: function (data) {
            if (data.res == 0)
                $('#l_errmsg').show().html('用户名或密码错误!');
            else if (data.res == 1)
                location.href = '/index';
            else if (data.res == 2)
                $('#l_errmsg').show().html('数据不完整');
            else if (data.res == 3)
                $('#l_errmsg').show().html('该用户未激活');
            else
                $('#l_errmsg').show().html('验证码错误');
        }
    })
}
