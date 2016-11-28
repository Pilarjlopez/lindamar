(function($){
  $(function(){

    //var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};

    // Plugin initialization
    $('.carousel.carousel-slider').carousel({full_width: true});
    $('.carousel').carousel();
    $('.slider').slider({full_width: true});
    $('.parallax').parallax();
    $('.modal-trigger').leanModal();
    $('.scrollspy').scrollSpy();
    $('.button-collapse').sideNav({'edge': 'left'});
    $('.datepicker').pickadate({selectYears: 20});
    $('select').not('.disabled').material_select();

    var window_width = $(window).width();

    $(window).scroll(function() {
        var altura_cabecera = $('.parallax-container').outerHeight(true);
        var altura_menu = $('.menu').outerHeight(true);

        if ($(window).scrollTop() >= altura_cabecera){
            $('.parallax-container').addClass('hide');
            $('.menu').addClass('navbar-fixed');
            $('#contenido').css('margin-top', '600px');
            $('#inicio a').replaceWith( '<a href="{{ url_for(' + 'curia.inicio' + ') }}" style="padding: 0 0 0 60px;"><img class="responsive-img" src="{{ url_for(' + 'static' + ', filename=' + 'img/escudo_curia.svg' + ') }}" style="width: 64px;height: 64px;"></a>' );
        } else {
            $('.parallax-container').removeClass('hide');
            $('.menu').removeClass('navbar-fixed');
            $('#contenido').css('margin-top', '0');
            $('#inicio a').replaceWith( '<a href="{{ url_for(' + 'curia.inicio' + ') }}">Inicio</a>' );
        }
    });

  }); // end of document ready
})(jQuery); // end of jQuery name space
