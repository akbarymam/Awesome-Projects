$('.page-scroll').on('click', function(){

var tujuan = $(this).attr('href');
var elemenTujuan = $(tujuan);
$('html,body').animate({
    scrollTop: elemenTujuan.offset().top -30
});
});