if($(window).width() < 992){
    $(".navbar").addClass("bg-white");
    console.log($(window).width());
}




$(function () {
  $(document).scroll(function () {
    var $nav = $(".navbar");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height()-70);
  });
});
