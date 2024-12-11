'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const opElem = document.getElementById('target');

for (let student of students) {
  const tarElem = document.createElement('option');
  tarElem.setAttribute('value', student.id);
  let tartElem = document.createTextNode(student.name);
  tarElem.appendChild(tartElem);
  opElem.appendChild(tarElem);
}