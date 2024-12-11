'use strict';
const names = ['John', 'Paul', 'Jones'];

const ulElem = document.querySelector('#target');

for (let name of names) {
  const liElem = document.createElement('li');
  liElem.textContent = `${name}`;
  ulElem.appendChild(liElem);
}