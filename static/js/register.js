$(function () {
    var error_name = false;
    var error_password = false;
    var error_check_password = false;
    $('#user_name').blur(function () {
        check_user_name();
    });
    $('#pwd').blur(function () {
        check_pwd();
    });
    $('#cpwd').blur(function () {
        check_cpwd();
    });

    function check_user_name() {
        var len = $('#user_name').val().length;
        if (len < 3 || len > 20) {
            $('#user_name').next().html('请输入3-20个字符的用户名')
            $('#user_name').next().show();
            error_name = true;
        } else {
            $('#user_name').next().hide();
            error_name = false;
        }
    }

    function check_pwd() {
        var len = $('#pwd').val().length;
        if (len < 6 || len > 20) {
            $('#pwd').next().html('密码最少6位，最长20位')
            $('#pwd').next().show();
            error_password = true;
        } else {
            $('#pwd').next().hide();
            error_password = false;
        }
    }

    function check_cpwd() {
        var pass = $('#pwd').val();
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

    $('#reg_form').submit(function () {
        check_user_name();
        check_pwd();
        check_cpwd();
        if (error_name == false && error_password == false && error_check_password == false) {
            return true;
        } else {
            return false;
        }
    });
})