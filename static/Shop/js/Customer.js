jQuery(document).ready(function(){
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    var CSRFTokenValue=getCookie('csrftoken');
    $('#regFormOpen').on('click', function(e){
        e.preventDefault();
        $("#regForm").css('display', 'block');
        $("#logForm").css('display', 'none');
    });
    $('#regForm').on('submit', function(e){
        e.preventDefault();
        var myData={};
        var password=$('#reg_password').val();
        var reg_password=$('#r_password').val();
        if(password===reg_password){
            myData.password=password;
            var myUrl=$(this).attr('action');
            myData['csrfmiddlewaretoken']=CSRFTokenValue;
            myData.password=password;
            myData.email=$('#reg_email').val();
            myData.name=$('#reg_name').val();
            myData.birthday=$('#birthday').val();
            console.log("Send form");
            $.ajax({
                url: myUrl,
                type: 'POST',
                data: myData,
                cache: true,
                success: function(result){
                    console.log(result);
                    switch(result.status){
                        case 'success' : alert("Регистрация прошла успешно");
                        $('#loginText').text(result.email);
                        break;
                        case 'exist': alert("Пользователь с таким email уже существует");
                        break;
                        default : alert("Упс");
                    }
                },
                error: function(jqXHR, textStatus, errorThrown){
                    alert("Missing some error: "+jqXHR+"; "+textStatus+"; "+errorThrown);
                }
            });
        }
        else{
            console.log('Error password');
            $('#reg_password').addClass('error_field');
            $('#reg_password').after('<p style="color:red">Пароли не совпадают!!!</p>');
            $('#r_password').addClass('error_field');
            $('#r_password').after('<p style="color:red">Пароли не совпадают!!!</p>');
        }        
    });
    $('#logForm').on('submit', function(e){
        e.preventDefault();
        var myData={}
        myData.email=$('#email').val();
        console.log(myData.email);
        myData.password=$('#password').val();
        myData['csrfmiddlewaretoken']=CSRFTokenValue;
        var myUrl=$(this).attr('action');
        $.ajax({
            url: myUrl,
            type: 'POST',
            data: myData,
            cache: true,
            success: function(result){
                console.log(result);
                switch(result.status){
                    case 'success' : alert("Авторизация прошла успешно");
                    $('#loginText').text(result.email);
                    break;
                    case 'email': alert("Пользователь с таким email не существует");
                    break;
                    case 'password': alert("Вы ввели неверный пароль");
                    break;
                    default : alert("Упс");
                }
            },
            error: function(jqXHR, textStatus, errorThrown){
                alert("Missing some error: "+jqXHR+"; "+textStatus+"; "+errorThrown);
            }
        });
    });
});