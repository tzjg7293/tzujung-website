var c = document.getElementById("circle");
var ctx = c.getContext("2d");
ctx.beginPath();
ctx.arc(100, 75, 80, 0, 2 * Math.PI);
ctx.stroke();
