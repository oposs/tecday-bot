
import { setCss, newEl } from './popper_util.js';
import Score from './popper_score.js';

export default class Sprite {
    static #screenWidth = window.innerWidth;
    static #screenHeight = window.innerHeight;
    #type = Math.random() > 0.5 ? 'good' : 'bad';
    #speed = Math.random() * 10 + 5;
    #alive = true;
    gameOver = false;
    #x;
    #y;
    #el;
    #score;

    constructor () {
        this.#score = new Score();
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
            backgroundColor: this.#type == 'bad' ? 'rgba(255,50,255,1)' : 'rgba(0,200,0,1)',
            transition: 'transform 0.5s, background-color 0.5s',
            zIndex: 10,
        });
        this.#el.addEventListener('pointerdown', (e) => {
            e.preventDefault();
            this.explode(this.#type);
        });
    }


    next () {
        this.#y += Math.round(this.#speed);
        if (this.#y > Sprite.#screenHeight) {
            if (this.#type == 'good') {
                this.#score.up();
            }
            else {
                this.explode('final');
                return true;
            }
        }
        if (!this.gameOver && this.#y > Sprite.#screenHeight || !this.#alive) {
            this.#el.remove();
            return false;
        }
        setCss(this.#el, {
            top: this.#y + 'px',
        });
        return true;
    }

    explode (type = this.#type) {

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
        setTimeout(() => {
            this.#alive = false;
            if (type != 'bad') {
                this.gameOver = true;
            }
        }, 600);
    }
    
}
