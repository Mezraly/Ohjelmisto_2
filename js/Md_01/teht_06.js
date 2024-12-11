const kysy = confirm("Should I calculate the square root?")

if (kysy === true){
  const num = parseInt(prompt("Number: "))
  vastaus = Math.sqrt(num)
}
else{
  vastaus = "The square root is not calculated."
}

const tAlue = document.querySelector('#tulosalue')
tAlue.innerHTML = `${vastaus}`