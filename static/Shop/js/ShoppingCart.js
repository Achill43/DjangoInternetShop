$(document).ready(function(){
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
    var deleteUrl=$('.deleteCart').attr('action');
    var CSRFTokenValue=getCookie('csrftoken');
    //console.log(deleteUrl);
    //console.log(CSRFTokenValue);
    $('body').on('click', '.deleteCart', function(e){
        e.preventDefault();
        var myData={};
        myData.productId=$(this).attr('id');
        deleteUrl=$(this).attr('action');
        myData['csrfmiddlewaretoken']=CSRFTokenValue;
        var myUrl=$(this).attr('action');
        $.ajax({
            url: myUrl,
            type: 'POST',
            data: myData,
            cache: true,
            success: function(result){
                $("#cartList").html('');
                $('.cartprice').text(result.totalPrice);
                for (var key in result.products) {
                    $('#cartList').append('<tr> <td>'+result.products[key].name+
                '</td>  <td>'+result.products[key].price+'</td>  <td>'+result.products[key].quantity+
                '</td> <td class="text-right"><a action="'+myUrl+'" class="btn deleteCart" id="'+key+'"><i class="fas fa-trash-alt"></i></a> </td> </tr>');
                }
            },
            error: function(jqXHR, textStatus, errorThrown){
                alert("Missing some error: "+jqXHR+"; "+textStatus+"; "+errorThrown);
            }
        });
    });
    $('.addToCart').click(function(e){
        e.preventDefault();
        var myData={};
        myData.productId=$(this).children('.basketBtn').attr('id');
        var csrfToken=$(this).children('input[name="csrfmiddlewaretoken"]').val();
        myData['csrfmiddlewaretoken']=csrfToken;
        var myUrl=$(this).attr('action');
        $.ajax({
            url: myUrl,
            type: 'POST',
            data: myData,
            cache: true,
            success: function(result){
                $("#cartList").html('');
                $('.cartprice').text(result.totalPrice);
                for (var key in result.products) {
                    $('#cartList').append('<tr> <td>'+result.products[key].name+
                '</td>  <td>'+result.products[key].price+'</td>  <td>'+result.products[key].quantity+
                '</td>  <td class="text-right"><a action="'+deleteUrl+'" class="btn deleteCart" id="'+key+'"><i class="fas fa-trash-alt"></i></a> </td> </tr></tr>');
                  }
                
            },
            error: function(jqXHR, textStatus, errorThrown){
                alert("Missing some error: "+jqXHR+"; "+textStatus+"; "+errorThrown);
            }
        });
    });
});