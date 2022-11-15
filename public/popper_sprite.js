
import { setCss, newEl } from './popper_util.js';
import Score from './popper_score.js';
import SpriteStore from './popper_spritestore.js';

export default class Sprite {
    static #screenWidth = window.innerWidth;
    static #screenHeight = window.innerHeight;
    static #score = new Score();
    static #ss = new SpriteStore();
    #type = Math.random() > 0.5 ? 'good' : 'bad';
    #speed = Math.random() * 10 + 5;
    #alive = true;
    gameOver = false;
    #x;
    #y;
    #el;

    constructor() {
        let r = 30;
        this.#x = Math.random() * (Sprite.#screenWidth - 4 * r) + r;
        this.#y = -2 * r;
        this.#el = newEl('div', {
            position: 'absolute',
            top: this.#y + 'px',
            left: this.#x + 'px',
            transform: 'scale(1)',
            borderRadius: this.#type == 'good' ? r + 'px' : '0px',
            transform: 'rotate(134deg)',
            width: (r * 2) + 'px',
            height: (r * 2) + 'px',
            backgroundColor: this.#type == 'bad' 
            ? 'rgba(255,50,255,1)' 
            : 'rgba(0,200,0,1)',
            transition: 'transform 0.5s, background-color 0.5s',
            zIndex: 10,
        });
        this.#el.addEventListener('pointerdown', (e) => {
            e.preventDefault();
            this.explode();
        });
    }


    step() {
        this.#y += Math.round(this.#speed);
        setCss(this.#el, {
            top: this.#y + 'px',
        });
        if (this.#y > Sprite.#screenHeight) {
            if (this.#type == 'good') {
                Sprite.#score.up();
                this.remove();
            }
            else {
                this.explode('final');
            }
        }
    }
    remove() {
        this.#el.remove();
        Sprite.#ss.delete(this);
    }
    explode(type = this.#type) {

        switch (type) {
            case 'bad':
                setCss(this.#el, {
                    backgroundColor: 'rgba(255,255,255,0)',
                    transform: 'scale(10) rotate(-135deg)',
                    zIndex: 1,
                });
                break;
            case 'good':
                setCss(this.#el, {
                    backgroundColor: 'rgba(255,0,0,1)',
                    transform: 'scale(100)',
                    zIndex: 1,
                });
                break;
            case 'final':
                setCss(this.#el, {
                    backgroundColor: 'rgba(0,0,0,1)',
                    transform: 'scale(100)',
                    zIndex: 1,
                });
                break;
        }
        this.#el.addEventListener('transitionend', (e) => {
            this.remove();
            if (type == 'good' || type == 'final') {
                Sprite.#ss.forEach((sprite) => {
                    sprite.remove();
                });
            }
        }, {
            once: true
        });
    }

}
