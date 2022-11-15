import GameOver from './popper_gameover.js';
import Sprite from './popper_sprite.js';
import SpriteStore from './popper_spritestore.js';

const interval = 50;

function main (e) {
    let ss = new SpriteStore();
    ss.add(new Sprite());
    let go = new GameOver();
    go.main = main;
    let loopId = setInterval(() => {
        if (Math.random() > 0.9) {
            ss.add(new Sprite());
        }
        ss.forEach((sprite) => {
            sprite.step();
        });
        if (ss.size == 0) {
            clearInterval(loopId);
            go.show();
        }
    }, interval);
    
}

window.addEventListener('DOMContentLoaded',main);
