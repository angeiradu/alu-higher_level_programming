$(document).ready(function () {
 $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json",
	  function (data) {
            data.results.forEach(function (film) {
              $("<li>").text(data.title).appendto("UL#list_movies");
	    });
	  });
});
