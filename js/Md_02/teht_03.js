let dogs = [];

dogs[0] = prompt("Dog 1: ");
dogs[1] = prompt("Dog 2: ");
dogs[2] = prompt("Dog 3: ");
dogs[3] = prompt("Dog 4: ");
dogs[4] = prompt("Dog 5: ");
dogs[5] = prompt("Dog 6: ");

dogs.sort().reverse();

let listHTML = '<ul>';
dogs.forEach(name => {
    listHTML += `<li>${name}</li>`;
});

listHTML += '</ul>';

document.getElementById('tulosalue').innerHTML = listHTML;