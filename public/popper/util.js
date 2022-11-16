
export function setCss(el, map) {
    Object.entries(map).forEach(([key, value]) => {
        el.style[key] = value;
    });
    return el;
}

export function newEl(tag, map, parent = document.body) {
    let el = document.createElement(tag);
    parent.append(el);
    setCss(el, map);
    return el;
}
