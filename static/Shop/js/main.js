$(document).ready(function(){
    'use srtict';
    var showing=false;
   $('#show_navbar').click(function(){
                                $('.collapse').toggle();
    });
    
    var slideWidth=0;
    var countSlides=$('.slider_block').length;
    var maxWidth=countSlides*340-2*340;
    $('.drop-btn').on('click', function(e){
        e.preventDefault();
        $(".dropdown-menu").css('display', 'none');
        if(showing==false){
            $(this).next(".dropdown-menu").fadeIn(1500);
        }
        else {
            $(this).next(".dropdown-menu").fadeOut(1500);
        }
        showing=!(showing);
    });
    $("#nextS").click(function(){
        slideWidth=slideWidth-340;
        console.log("before: "+slideWidth);
        if(slideWidth*(-1)<maxWidth){
            $('.slider_hots').animate({'margin-left': +slideWidth}, 2000);
        }
        else{
            slideWidth=slideWidth+340;
        }
        console.log("after: "+slideWidth);
    });
    $("#prevS").click(function(){
        slideWidth=slideWidth+340;
        if(slideWidth<=0){
            $('.slider_hots').animate({'margin-left': +slideWidth}, 2000);
        }
        else{slideWidth=0;}
    });
    
    $(window).scroll(function(){
        var scrollValue=$(this).scrollTop();
        if(scrollValue<=72){
            $('#menuBg').css("position", "static");
            $('#menuBg').css("left", "0");
            $('#menuBg').css("margin-left", "0px");
            $('#menuBg').css("margin-top", "10px");
        }
        else{
            $('#menuBg').css("position", "fixed");
            $('#menuBg').css("left", "50%");
            $('#menuBg').css("margin-left", "-50%");
            $('#menuBg').css("margin-top", "-73px");
            $('#menuBg').css("z-index", "100");
        }
    });
});