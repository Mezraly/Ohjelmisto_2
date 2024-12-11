let numerot = [];
numerot[0] = parseInt(prompt("Number 1: "));
numerot[1] = parseInt(prompt("Number 2: "));
numerot[2] = parseInt(prompt("Number 3: "));
numerot[3] = parseInt(prompt("Number 4: "));
numerot[4] = parseInt(prompt("Number 5: "));

let reversed = [];
for (let i = numerot.length - 1; i >= 0; i--) {
  reversed.push(numerot[i]);
}

for (let i = 0; i < reversed.length; i++) {
        console.log `${reversed[i]}`
    }
