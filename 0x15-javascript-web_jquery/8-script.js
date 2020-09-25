#!/usr/bin/node

$(document).ready( function () {
        $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
                let items = [];
                $.each( data.results, function (index, value) {
                        items.push('<li>'+value.title+'</li>');
                });
                $.each( items, function (index, value) {
                        $('ul#list_movies').append(value);
                });
        });
});