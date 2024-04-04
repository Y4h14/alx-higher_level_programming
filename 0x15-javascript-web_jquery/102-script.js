#!/usr/bin/node
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.get('https://hellosalut.stefanbohacek.dev/?' + $.param({ lang: $('INPUT#language_code').val() }),
      function (data) {
        $('DIV#hello').html(data.hello);
      });
  });
});
