let number = parseInt(prompt("Enter an integer:"));

if (number <= 1) {
    document.getElementById("tulosalue").innerText = `${number} is not a prime number.`;
} else {

  let isPrime = true;
  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) {
      isPrime = false;
      break;
    }
  }
  if (isPrime) {
    document.getElementById("tulosalue").innerText = `${number} is a prime number.`;
  } else {
      document.getElementById("tulosalue").innerText = `${number} is not a prime number.`;
  }
}


