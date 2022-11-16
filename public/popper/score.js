import { newEl } from './util.js';

export default class Score {
    static #instance;
    static #value = 0;
    static #el = newEl('div', {
        position: 'absolute',
        top: '20px',
        right: '20px',
        fontFamily: 'sans-serif',
        fontSize: '30px',
        height: '30px',
    });
    constructor () {
        if (! Score.#instance ) {
            Score.#instance = this;
        }
        return Score.#instance;
    }
    
    get value () {
        return Score.#value;
    }

    up () {
        Score.#value++;
        Score.#el.textContent = 'Score: ' + Score.#value;
    };
}