    $.ajaxSetup({
    data: {csrfmiddlewaretoken: '{{ csrf_token }}'}
})
//点击登录按钮 ，提交数据
function login() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    $.ajax({
        'url': '/login/',
        'type': 'post',
        'data': {'username': username, 'password': password},
        'dataType': 'json',
        success: function (data) {
            if (data.res == 1)
                location.href = '/index';
            else {
                $('#errormessage').show().html('用户名或密码错误!');
            }
        }
    })
}