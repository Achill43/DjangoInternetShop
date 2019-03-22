$(document).ready(function()
{
var slideIndex=1;
var slides = $(".slide");
var dots = $('.dot');
function showSlides(n){
    var i;
    //console.log(slides.length);
    //console.log(slides);
    //console.log(dots);
    if(n>slides.length){
        slideIndex=1;
    }
    if(n<1){
        slideIndex=slides.length;
    }
    for(i=0; i<slides.length; i++)
        {slides[i].style.display="none";}
    for(i=0; i<dots.length; i++)
        {dots[i].className=dots[i].className.replace("active", "");}
    slides[slideIndex-1].style.display="block";
    dots[slideIndex-1].className+=" active";
}
showSlides(slideIndex);
    $(".dot").click(function(){
        var clickId=$(this).attr('id');
        currentSlide(clickId);
    });
function plusSlides(n){
    showSlides(slideIndex+=n);
}
function currentSlide(n){
    showSlides(slideIndex=n);
}
setInterval(function()
	{
        for(i=0; i<slides.length; i++)
        {slides[i].style.display="none";}
        for(i=0; i<dots.length; i++)
        {dots[i].className=dots[i].className.replace("active", "");}
		$(slides[slideIndex-1]).css('display', 'block');
    
        dots[slideIndex-1].className+=" active";
        slideIndex++;
		if(slideIndex===slides.length+1)
		{
            for(i=0; i<slides.length; i++)
            {slides[i].style.display="none";}
            for(i=0; i<dots.length; i++)
            {dots[i].className=dots[i].className.replace("active", "");}
            slideIndex=1;
		    $(slides[slideIndex-1]).css('display', 'block');
        }
	},1500);
});