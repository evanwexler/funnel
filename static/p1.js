// var cbwaypoint = new Waypoint({
//     context: $("div.main"),
//     element: $("div.colourbar"),
//     handler: function(d) {
//       if (d == 'down') {
//       $("div.main").unbind('scroll', scrollFunc);
//       $('nav.nav').css({'z-index':1});
//         if ($('nav.nav').has('div.colourbar').length == 0) {
//             $('nav.nav').append($('div.colourbar')[0].outerHTML)
//             }
//       }
//       else {
//       $("div.main").bind('scroll', scrollFunc)
//       $('nav.nav').css({'z-index':-1})
//           $('nav.nav div.colourbar').remove()
//       }
//     },
//     offset: '100px',
//     })

var page1height = $("div.page1").innerHeight();

var pagesLoaded = []

// scrollFunc = function() {
//     scrolltop = $(this).scrollTop()
//     $("img.mainlogo").height(300-scrolltop)
//     $("div.downarrow").height(200-scrolltop)
//     $("div.page1").height(page1height-scrolltop)
//     $("div.page1").css({'margin-top':scrolltop})
// }

loadNextPage = function() {
    if($(this).scrollTop() + $(this).innerHeight() >= $(this)[0].scrollHeight) {
    url = $('a.nextpage:last').attr('href')
    isPresent = pagesLoaded.indexOf(url)
    if (isPresent == -1) {
      pagesLoaded.push(url)
    x = $.get(url, function(data) {
      content = $('div.main', data)[0]
      $("div.main").append(content.innerHTML)
        })
    }
    }
}

// $('div.main').bind('scroll', scrollFunc)
$('div.main').bind('scroll', loadNextPage)
