/*exported rangeBetween*/
/*eslint-env browser*/
/*eslint no-console:0*/
function rangeBetween(index1, index2) {
    var arr = new Array();
    var i = 0;
    while (index1 <= index2) {
        arr[i] = index1;
        i++;
        index1++;
    }
    document.write("[" + arr + "]<br>");
    return arr;
}

console.log(rangeBetween(4, 7));
console.log(rangeBetween(-4, 7));