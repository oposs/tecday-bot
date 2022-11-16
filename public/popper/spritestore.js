export default class SpriteStore {
    static #instance;
    static #data = new Set();
    constructor () {
        if (! SpriteStore.#instance ) {
            SpriteStore.#instance = this;
        }
        return SpriteStore.#instance;
    }
    forEach(cb) {
        return SpriteStore.#data.forEach(cb);
    }
    delete(instance) {
        return SpriteStore.#data.delete(instance);
    }
    add(instance) {
        return SpriteStore.#data.add(instance,1);
    }
    get size() {
        return SpriteStore.#data.size;
    }
}