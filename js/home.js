let stars = document.getElementById("stars");
let moon = document.getElementById("moon");
let mountains_behind = document.getElementById("mountains_behind");
let mountains_front = document.getElementById("mountains_front");
let text = document.getElementById("text");
let btn = document.getElementById("btn");
let header = document.querySelector('header');
let navbar_li = $(".navbar ul li");

// Let stars move across sky as you scroll
window.addEventListener('scroll', function () {
    let value = window.scrollY;
    var rbg = value / 5 * 0.01;
    console.log("rbg: " + rbg);
    stars.style.left = value * 0.25 + 'px';
    moon.style.top = value * 1.05 + 'px';
    mountains_behind.style.top = value * 0.5 + 'px';
    mountains_front.style.width = 100 + value / 15 + "%";
    // text.style.marginRight = value * 4 + 'px';
    text.style.marginTop = value * 1.5 + 'px';
    // btn.style.marginTop = value * 1.5 + 'px';
    console.log("ScrollY: " + window.scrollY)
    if (window.scrollY > 50) {
        // header.classList.add('scroll-active');
        // header.style.backgroundColor = "rgb(129, 112, 145, " + value / 5 * 0.01 + ")";
        if (rbg < 1) {
            console.log(rbg)
            header.style.backgroundColor = "rgb(255, 255, 255, " + rbg + ")";
        }
        else {
            header.style.backgroundColor = "rgb(255, 255, 255, 0.5)"
        }
        $('header ul li a').css('color', 'black');
    }
    else {
        // header.style.backgroundColor = "rgb(129, 112, 145, 0)";
        header.style.backgroundColor = "rgb(255, 255, 255, 0)";
        $('header ul li a').css('color', 'white');
        // $('header ul li a:hover').css('color', 'black');
    }
})