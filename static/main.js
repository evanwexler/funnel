showMore = function() {
  url = $('a.nextpage').attr('href')
  x = $.get(url, function(data) {
      links = $('img.gifs', data)
      for (var i = 0; i<links.length; i++) {
      $('div.main').append(links[i].outerHTML)
      }
      })
}

var waypoint = new Waypoint({
    context: $('div.main'),
    element: $('div.main .end'),
    handler: function(d) {
    showMore()
    }
    })
