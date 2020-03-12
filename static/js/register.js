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

$(function () {
    var error_name = false;
    var error_password = false;
    var error_check_password = false;
    var error_email = false;
    $('#r_username').blur(function () {
        check_user_name();
    });
    $('#r_pwd').blur(function () {
        check_pwd();
    });
    $('#cpwd').blur(function () {
        check_cpwd();
    });
    $('#email').blur(function () {
        check_email();
    });


    function check_user_name() {
        var len = $('#r_username').val().length;
        if (len < 3 || len > 20) {
            $('#r_username').next().html('请输入3-20个字符的用户名')
            $('#r_username').next().show();
            error_name = true;
        } else {
            $('#r_username').next().hide();
            error_name = false;
        }
    }

    function check_pwd() {
        var len = $('#r_pwd').val().length;
        if (len < 6 || len > 20) {
            $('#r_pwd').next().html('密码最少6位，最长20位')
            $('#r_pwd').next().show();
            error_password = true;
        } else {
            $('#r_pwd').next().hide();
            error_password = false;
        }
    }

    function check_cpwd() {
        var pass = $('#r_pwd').val();
        var cpass = $('#cpwd').val();
        if (pass != cpass) {
            $('#cpwd').next().html('两次输入的密码不一致')
            $('#cpwd').next().show();
            error_check_password = true;
        } else {
            $('#cpwd').next().hide();
            error_check_password = false;
        }
    }

    function check_email() {
        var re = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if (re.test($('#email').val())) {
            $('#email').next().hide();
            error_email = false;
        } else {
            $('#email').next().html('邮箱格式不正确');
            $('#email').next().show();
            error_email = true;
        }
    }


    $('#reg_form').submit(function () {
        check_user_name();
        check_pwd();
        check_cpwd();
        if (error_name == false && error_password == false && error_check_password == false && error_email == false) {
            return true;
        } else {
            return false;
        }
    });
})


function register() {
    let username = document.getElementById("r_username").value;
    let password = document.getElementById("r_pwd").value;
    let cpwd = document.getElementById("cpwd").value;
    let email = document.getElementById("email").value;
    $.ajax(
        {
            'url': '/register/',
            'type': 'post',
            'data': {
                'username': username,
                'password': password,
                'cpwd': cpwd,
                'email': email
            },
            'dataType': 'json',
            success: function (data) {
                if (data.res == 1)
                    location.href = '/register_success/';
                else if (data.res == 2)
                    $('#r_errmsg').show().html('数据不完整');
                else
                    $('#r_errmsg').show().html('该用户名已存在');
            }
        })
}