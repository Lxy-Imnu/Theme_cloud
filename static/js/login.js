$.ajaxSetup({
    data: {csrfmiddlewaretoken: '{{ csrf_token }}'}
})

//点击登录按钮 ，提交数据
function login() {
    let username = document.getElementById("l_username").value;
    let password = document.getElementById("l_pwd").value;
    // let code = document.getElementById("code").value;
    $.ajax({
        'url': '/login/',
        'type': 'post',
        'data': {
            'username': username,
            'password': password,
            // 'code': code,
        },

        'dataType': 'json',
        success: function (data) {
            if (data.res == 0)
                $('#errmsg').show().html('用户名或密码错误!');
            else if (data.res == 1)
                location.href = '/index';
            else if (data.res == 2)
                $('#errmsg').show().html('数据不完整');
            else if (data.res == 3) {
                $('#errmsg').show().html('该用户未激活');
            // else
            //     $('#errmsg').show().html('验证码错误');

            }
        }
    })
}