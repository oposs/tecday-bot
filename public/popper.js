import GameOver from './popper_gameover.js';
import Score from './popper_score.js';
import Sprite from './popper_sprite.js';

const interval = 50;

function main (e) {
    let score = new Score();
    let spriteList = [];
    let loopId = setInterval(() => {
        if (Math.random() > 0.9) {
            spriteList.push(new Sprite(score));
        }
        let recyclingList = [];
        spriteList.forEach((sprite, i) => {
            if (!sprite.next()) {
                recyclingList.unshift(i);
            }
            if (sprite.gameOver) {
                clearInterval(loopId);
                new GameOver(score.value);
            }
        });
        recyclingList.forEach((i) => {
            spriteList.splice(i, 1);
        });
    }, interval);
}

window.addEventListener('DOMContentLoaded',main);
