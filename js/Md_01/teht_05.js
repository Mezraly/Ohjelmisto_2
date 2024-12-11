'use strict';

const lukustr = prompt("Anna luku: ")
const luku = parseInt(lukustr)


if (luku % 4 === 0 && luku % 100 !== 0) {
    vastaus = "on"
}

if (luku % 4 === 0 && luku % 100 !== 0 && luku % 400 === 0) {
    vastaus = "on"
}

else {
    vastaus = "on"
}

let vastaus = `${luku} ${vastaus} karkausvuosi`
const tAlue = document.querySelector('#tulosalue')
tAlue.innerHTML = `${vastaus}`