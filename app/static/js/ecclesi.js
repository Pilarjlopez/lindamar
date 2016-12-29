(function($){
  $(function(){

    var window_width = $(window).width();
    var window_height = $(window).height();
    $('.block').css('height', window_height + 'px');

    // Plugin initialization
    $('.carousel.carousel-slider').carousel({full_width: true});
    //$('.carousel').carousel();
    $('.slider').slider({full_width: true});
    $('.parallax').parallax();
    $('.modal-trigger').leanModal();
    $('.scrollspy').scrollSpy();
    $('.button-collapse').sideNav({'edge': 'left'});
    $('.datepicker').pickadate({selectYears: 20});
    $('select').not('.disabled').material_select();

    $(window).scroll(function() {
        var altura_cabecera = $('.parallax-container').outerHeight(true);
        var altura_menu = $('.menu').outerHeight(true);

        if ($(window).scrollTop() >= altura_cabecera){
            $('#cabecera').addClass('hide');
            $('.menu').addClass('navbar-fixed');
            $('#contenido').css('margin-top', '600px');
            //$('#inicio a').replaceWith( '<a href="{{ url_for(' + 'curia.inicio' + ') }}" style="padding: 0 0 0 60px;"><img class="responsive-img" src="{{ url_for(' + 'static' + ', filename=' + 'img/escudo_curia.svg' + ') }}" style="width: 64px;height: 64px;"></a>' );
        } else {
            $('#cabecera').removeClass('hide');
            $('.menu').removeClass('navbar-fixed');
            $('#contenido').css('margin-top', '0');
            //$('#inicio a').replaceWith( '<a href="{{ url_for(' + 'curia.inicio' + ') }}">Inicio</a>' );
        }
    });

    var window_width = $(window).width();
    var window_height = $(window).height();

    var roller_alto = $('#roller ul').height();
    $('#roller ul').css('top', ((window_height / 2) - roller_alto) + 'px');
    $('.block').css('height', window_height + 'px');

    var pie_alto = $('.pie-seccion').height();

    // Seccion 1
    var contenido1_alto = $('#seccion1 .contenido').height();
    $('#seccion1 .contenido').css('margin-top', ((window_height / 2) - contenido1_alto) + 'px');
    $('#seccion1 .pie-seccion').css('margin-top', (window_height - pie_alto) + 'px');

    // Seccion 2
    var contenido2_alto = $('#seccion2 .contenido').height();
    //$('#seccion2 .contenido').css('margin-top', (((window_height / 2) + window_height) - contenido2_alto) + 'px');
    //$('#seccion2 .pie-seccion').css('margin-top', ((window_height * 2) - pie_alto) + 'px');

    // Seccion 3
    var contenido3_alto = $('#seccion3 .contenido').height();
    //$('#seccion3 .contenido').css('margin-top', (((window_height / 2) + (window_height * 2)) - contenido3_alto) + 'px');
    //$('#seccion3 .pie-seccion').css('margin-top', ((window_height * 3) - pie_alto) + 'px');

  }); // end of document ready
})(jQuery); // end of jQuery name space
