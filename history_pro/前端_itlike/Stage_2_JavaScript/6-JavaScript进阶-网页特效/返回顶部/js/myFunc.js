/**
 * 获取滚动的头部距离和左边距离
 * scroll().top scroll().left
 * @returns {*}
 */
function scroll() {
    if(window.pageYOffset !== null){
        return {
            top: window.pageYOffset,
            left: window.pageXOffset
        }
    }else if(document.compatMode === "CSS1Compat"){ // W3C
        return {
            top: document.documentElement.scrollTop,
            left: document.documentElement.scrollLeft
        }
    }

    return {
        top: document.body.scrollTop,
        left: document.body.scrollLeft
    }
}

/**
 * 用于获取标签的函数(通过id)
 * @param id
 * @returns {any}
 */
function $(id) {
    return typeof id === "string" ? document.getElementById(id) : null;
}

/**
 * 用于展示的函数
 * @param obj
 * @returns {string}
 */
function show(obj) {
    return obj.style.display = 'block';
}

/**
 * 用于隐藏的函数
 * @param obj
 * @returns {string}
 */
function hide(obj) {
    return obj.style.display = '';
}
