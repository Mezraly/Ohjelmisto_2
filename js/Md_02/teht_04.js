let numbers = [];
while (true) {
  let num = parseInt(prompt("Enter a number (0 to stop):"));
  if (num === 0) break;
  numbers.push(num);
}
numbers.sort((a, b) => b - a);

for (let numb of numbers) {
      console.log(`${numb}`);
    }