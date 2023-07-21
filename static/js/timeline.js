// TIMELINE FLIP
$('#medical-flip').click(function (e) {
  var $timeline = $('.timeline');
  var $timeline_subtitle = $(".timeline-header-subtitle-container");
  $('#medical-flip').css("background-color", "white");
  $('#medical-flip').css("color", "#f197a3");
  $('#software-flip').css("background-color", "#f197a3");
  $('#software-flip').css("color", "white");
  $timeline.addClass('flipped');
  $timeline_subtitle.addClass('flipped');
});
$('#software-flip').click(function (e) {
  var $timeline = $('.timeline');
  var $timeline_subtitle = $(".timeline-header-subtitle-container");
  $('#software-flip').css("background-color", "white");
  $('#software-flip').css("color", "#f197a3");
  $('#medical-flip').css("background-color", "#f197a3");
  $('#medical-flip').css("color", "white");
  $timeline.removeClass('flipped');
  $timeline_subtitle.removeClass('flipped');
});

// TIMELINE SCROLL ANIMATION
(function ($) {
  $.fn.timeline = function () {
    var selectors = {
      id: $(this),
      activeClass: "timeline-item--active",
      activeDate: "timeline-info--active",
      img: ".timeline__img"
    };

    var all_item = $('.timeline-item');
    var itemLength = all_item.length;

    $(window).scroll(function () {
      var max, min;
      var screen_height = screen.height;
      var pos = $(this).scrollTop();
      //console.log("Pos: " + pos);
      $(".timeline-item").each(function (i, item) {
        content = $('.timeline-content');
        date = $('.timeline-info');
        min = $(this).offset().top;
        max = ($(this).height() + min);
        var item_middle = min + (max - min) / 2;

        if (i == itemLength - 2 && (pos + screen_height / 3) > item_middle) {
          content.last().addClass(selectors.activeClass);
          date.last().addClass(selectors.activeDate);
          // selectors.item.removeClass(selectors.activeClass);
          // selectors.id.css("background-image", "url(" + selectors.item.last().find(selectors.img).attr('src') + ")"); //not sure what this is for, but it removes the after-lining of the box after transition
        } else if ((pos + screen_height / 3) <= max - 40 && (pos + screen_height / 3) >= min) {
          content.eq(i).addClass(selectors.activeClass);
          date.eq(i).addClass(selectors.activeDate);
          selectors.id.css("background-image", "url(" + $(this).find(selectors.img).attr('src') + ")");
          // selectors.item.removeClass(selectors.activeClass);
        }
      });
    });
  }
})(jQuery);
$("#timeline").timeline();
