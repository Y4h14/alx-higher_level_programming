#!/usr/bin/node
$(document).ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).on('keypress', function (e) {
      if (e.which === 13) { translate(); }
    });
  });
});
function translate () {
  $.get('https://hellosalut.stefanbohacek.dev/?' + $.param({ lang: $('INPUT#language_code').val() }),
    function (data) {
      $('DIV#hello').html(data.hello);
    });
}
