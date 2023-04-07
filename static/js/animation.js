import { Application } from '@splinetool/runtime';

const canvas = document.getElementById('canvas3d');
const cat = document.getElementById('cat-logo');
const app = new Application(canvas);
const cat_app = new Application(cat);

app.load('https://prod.spline.design/cz0BLZ815731ZTLl/scene.splinecode');
cat_app.load('https://prod.spline.design/PDV84pzIT2cb8s74/scene.splinecode');