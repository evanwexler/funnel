
showMore = function() {
  url = $('a.nextpage:last').attr('href')
  x = $.get(url, function(data) {
    content = $('div.main', data)[0]
    $("div.main").append(content.innerHTML)
      })
    // waypoint.disable()
    // waypoint.enable()
}


var waypoint = new Waypoint({
    context: $('div.main'),
    element: $('div.main .end:last'),
    offset: '100%',
    handler: function(d) {
    showMore()
    }
    })

