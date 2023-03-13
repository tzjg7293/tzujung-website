(function ($) {
  $.fn.timeline = function () {
    var selectors = {
      id: $(this),
      item: $(this).find(".timeline-item"),
      activeClass: "timeline-item--active",
      img: ".timeline__img"
    };
    selectors.item.eq(0).addClass(selectors.activeClass);
    // selectors.id.css("background-image", "url(" + selectors.item.first().find(selectors.img).attr("src") + ")");

    var itemLength = selectors.item.length;
    $(window).scroll(function () {
      var max, min;
      var screen_height = screen.height;
      // var pos = ($(this).scrollTop() + screen_height / 2);
      var pos = $(this).scrollTop();
      selectors.item.each(function (i) {
        console.log( i + ": " + $( this ).text());
        min = $(this).offset().top;
        max = ($(this).height() + $(this).offset().top);
        var item_middle = min + (max - min) / 2;
        // console.log("Curr item: " + i);
        // console.log("itemlength: " + itemLength);
        // console.log("Item Height: " + $(this).height());
        // console.log("Screen height: " + screen_height);
        // console.log("Pos: " + pos);
        // console.log("Item middle: " + item_middle);
        // console.log("Min: " + min);
        // console.log("Max: " + max);
        // console.log("midpoint: " + (item_middle + screen_height / 2));

        // var that = $(this)

        if (i == itemLength - 2 && (pos + screen_height/3) > item_middle) {
          selectors.item.removeClass(selectors.activeClass);
          selectors.id.css("background-image", "url(" + selectors.item.last().find(selectors.img).attr('src') + ")"); //not sure what this is for, but it removes the after-lining of the box after transition
          selectors.item.last().addClass(selectors.activeClass)
        } else if ((pos + screen_height/3) <= max - 40 && (pos + screen_height/3) >= min) {
          selectors.id.css("background-image", "url(" + $(this).find(selectors.img).attr('src') + ")");
          selectors.item.removeClass(selectors.activeClass);
          $(this).addClass(selectors.activeClass);
        }

      });
    });

  }
})(jQuery);
$("#timeline-1").timeline();