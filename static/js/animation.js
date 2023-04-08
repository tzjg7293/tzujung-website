import { Application } from '@splinetool/runtime';

const canvas = document.getElementById('canvas3d');
const cat = document.getElementById('cat-logo');
// const cursor_trail = document.getElementById('cursor-trail');

const app = new Application(canvas);
const cat_app = new Application(cat);
// const cursor_app = new Application(cursor_trail);

app.load('https://prod.spline.design/cz0BLZ815731ZTLl/scene.splinecode');
cat_app.load('https://prod.spline.design/PDV84pzIT2cb8s74/scene.splinecode');
// cursor_app.load('https://prod.spline.design/jmp7izZPfkM9SJaK/scene.splinecode');