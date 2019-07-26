if($(window).width() < 992){
    $(".navbar").addClass("bg-white");
}




$(function () {
  $(document).scroll(function () {
    var $nav = $(".navbar");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height()-70);
  });
});

var swiper = new Swiper('.sw-cn', {

  loop: true,
  autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
  pagination: {
    el: '.swiper-pagination1',
  },
});
