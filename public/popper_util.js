
export function setCss(el, map) {
    Object.entries(map).forEach(([key, value]) => {
        el.style[key] = value;
    });
    return el;
}

export function newEl(tag, map) {
    let el = document.createElement(tag);
    document.body.append(el);
    setCss(el, map);
    return el;
}
