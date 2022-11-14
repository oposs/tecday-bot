import { newEl } from './popper_util.js';
import Score from './popper_score.js';

export default class GameOver {
    static #instance;
    static #el;
    constructor () {
        if (! GameOver.#instance ) {
            GameOver.#instance = this;
            this.init()
        }
        return GameOver.#instance;
    }
    init () {
        GameOver.#el = newEl('div', {
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
            zIndex: '20'
        });
        GameOver.#el.innerText = (new Score()).value;
        const urlParams = new URLSearchParams(window.location.search);
        const uid = urlParams.get('uid');
        const mid = urlParams.get('mid');
        const cid = urlParams.get('cid');
        const imid = urlParams.get('imid');
        const request = new Request(imid
            ? `/setScore?uid=${uid}&imid=${imid}&score=${value}`
            : `/setScore?uid=${uid}&mid=${mid}&cid=${cid}&score=${value}`);
        fetch(request).then(response => console.log("set score",response));
    };
}