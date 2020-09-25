#!/usr/bin/node

$(document).ready(function () {
  const apiService = 'https://fourtonfish.com/hellosalut/?lang=';
  $('#btn_translate').click(function () {
    const toQuery = apiService + $('#language_code').val();
    $.getJSON(toQuery, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });

  $('#language_code').focus(function () {
    $(document).on('keypress', function (e) {
      if (e.which === 13) {
        const toQuery = apiService + $('#language_code').val();
        $.getJSON(toQuery, function (data) {
          $('DIV#hello').text(data.hello);
        });
      }
    });
  });
});
