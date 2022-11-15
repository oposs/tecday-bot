import { newEl } from './popper_util.js';
import Score from './popper_score.js';

export default class GameOver {
    static #instance;
    static #rootEl;
    static #scoreEl;
    static #main;
    static #score = new Score();
    constructor () {
        if (! GameOver.#instance ) {
            GameOver.#instance = this;
            this.init()
        }
        return GameOver.#instance;
    }
    init () {
        let root = newEl('div', {
            position: 'absolute',
            top: '0px',
            right: '0px',
            width: '100%',
            height: '100%',
            fontFamily: 'sans-serif',
            fontSize: '100px',
            backdropFilter: 'blur(5px)',
            backgroundColor: 'rgba(0,0,0,0.8)',
            color: '#fff',
            textAlign: 'center',
            lineHeight: '300px',
            zIndex: '20',
            visibility: 'hidden'
        });
        GameOver.#scoreEl = newEl('div',{
            position: 'absolute',
            top: '20%',
            width: '100%',
            textAlign: 'center'
        },root)
        let restart = newEl('div', {
            position: 'absolute',
            bottom: '30%',
            width: '100%',
            textAlign: 'center'
        },root);
        GameOver.#rootEl = root;
        restart.innerText = '→ New Game ←';

        restart.addEventListener('click',(e) => {
            // no recursion on restart
            this.hide();
            setTimeout(GameOver.#main(),0);
        });       
    }
    show () {
        GameOver.#rootEl.style.visibility = 'visible';
        GameOver.#scoreEl.innerText = 'Score: ' + (new Score()).value;
        this.#reportScore();
    }
    hide () {
        GameOver.#rootEl.style.visibility = 'hidden';
    }
    set main (value) {
        GameOver.#main = value;
    }
    #reportScore () {
        const urlParams = new URLSearchParams(window.location.search);
        const uid = urlParams.get('uid');
        const mid = urlParams.get('mid');
        const cid = urlParams.get('cid');
        const imid = urlParams.get('imid');
        const value = GameOver.#score.value;
        const request = new Request(imid
            ? `/setScore?uid=${uid}&imid=${imid}&score=${value}`
            : `/setScore?uid=${uid}&mid=${mid}&cid=${cid}&score=${value}`);
        fetch(request).then(response => console.log("set score",response));
    }
}