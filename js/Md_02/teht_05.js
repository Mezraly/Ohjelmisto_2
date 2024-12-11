let numbers = [];
while (true) {
  let num = parseInt(prompt("Enter a number:"));

  if (numbers.includes(num)) {
    alert(`Number ${num} was already entered.`)
    break;
  }
  numbers.push(num);
}

numbers.sort((a, b) => a - b);

console.log(numbers);