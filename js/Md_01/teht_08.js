let startYear = parseInt(prompt("Start year:"));
let endYear = parseInt(prompt("End year:"));
let leapYears = [];

for (let year = startYear; year <= endYear; year++) {
    if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
        leapYears.push(year);
    }
}

let list = document.getElementById("tulosalue");
list.innerHTML = "";

leapYears.forEach((year) => {
    let listItem = document.createElement("li");
    listItem.textContent = year;
    list.appendChild(listItem);
});
