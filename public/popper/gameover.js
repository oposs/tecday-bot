import { newEl } from './util.js';
import Score from './score.js';

export default class GameOver {
    static #instance;
    static #rootEl;
    static #scoreEl;
    static #reStartGame;
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
            fontSize: '10vw',
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
            top: '20vh',
            width: '100%',
            textAlign: 'center'
        },root)
        let restart = newEl('div', {
            position: 'absolute',
            bottom: '30vh',
            width: '100%',
            textAlign: 'center'
        },root);
        GameOver.#rootEl = root;
        restart.innerText = '→ New Game ←';

        restart.addEventListener('click',(e) => {
            // no recursion on restart
            this.hide();
            setTimeout(GameOver.#reStartGame(),0);
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
    set reStartGame (value) {
        GameOver.#reStartGame = value;
        GameOver.#score.reset();
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