#!/usr/bin/node

$(document).ready( function () {
        const apiService = 'https://fourtonfish.com/hellosalut/?lang=';
        $('#btn_translate').click( function () {
                const toQuery = apiService + $('#language_code').val();
                $.getJSON(toQuery, function (data) {
                        $('DIV#hello').text(data.hello);
                });
        });
});