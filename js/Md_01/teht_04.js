'use strict';

const nimi = prompt("Mikä on nimesi: ")

const tuvanNro = 1 + Math.floor( Math.random() * 4)

let tuvanNimi

if (tuvanNro == 1) {
    tuvanNimi = "Gryffindor"
} else if (tuvanNro == 2) {
    tuvanNimi = "Slytherin"
} else if (tuvanNro == 3) {
    tuvanNimi = "Hufflepuff"
} else if (tuvanNro == 4) {
    tuvanNimi = "Ravenclaw"
}

let vastaus = `Hei ${nimi}, tupasi on ${tuvanNimi}`

const tAlue = document.querySelector('#tulosalue')
tAlue.innerHTML = `${vastaus}`