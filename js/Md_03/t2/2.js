// etsitään <ul> määritys html sivulta
const ulElem = document.querySelector('#target');

// tehdään eka li-elementti
let li1Elem = document.createElement('li');
// tehtään tekstiElementti
let text1Elem = document.createTextNode('First item');
// lisätään li-elementin sisään eli lapseksi äsken luotu teksti-elementti
li1Elem.appendChild(text1Elem);
// toinen li-elementti, Huomaa lyhyempi tapa!
const li2Elem = document.createElement('li');
li2Elem.textContent = 'Second item';
li2Elem.classList.add('my-item');

const li3Elem = document.createElement('li');
li3Elem.textContent = 'Third item';

ulElem.appendChild(li1Elem);
ulElem.appendChild(li2Elem);
ulElem.appendChild(li3Elem);