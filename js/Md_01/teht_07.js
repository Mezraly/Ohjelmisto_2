let numberOfRolls = parseInt(prompt("How many dice would you like to roll?"));
let sum = 0;

for (let i = 0; i < numberOfRolls; i++) {
  let roll = Math.floor(Math.random() * 6) + 1; // Random number between 1 and 6
  sum += roll;
}
console.log(sum);