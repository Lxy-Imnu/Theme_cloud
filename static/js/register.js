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
    $('#eml').blur(function () {
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
            $('#email').next().hide()
            error_name = false;
        } else {
            $('#email').next().html('邮箱格式不正确')
            $('#email').next().show()
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
                    location.href = '/index';
                else if (data.res == 2)
                    $('#errmsg').show().html('数据不完整');
                else {
                    $('#errmsg').show().html('该用户名已存在');
                }
            }
        })
}