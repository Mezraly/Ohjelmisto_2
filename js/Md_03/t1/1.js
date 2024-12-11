const ulElem = document.querySelector('#target');

// lisätään sisältöä ulElem sisään
ulElem.innerHTML =
    `
     <li>First item</li>
     <li>Second item</li>
     <li>Third item</li>
    `
// määritellään ul-elementille tyylimääritys
ulElem.classList.add('my-list');