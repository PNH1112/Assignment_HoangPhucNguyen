'use strict';

const startYear = parseInt(prompt("Enter your start year:"));
const endYear = parseInt(prompt("Enter your end year"));

for (let i = startYear; i <= endYear; i++) {
    if ((i % 4 === 0 && i % 100 !== 0) || (i % 400 === 0)) {

        const li = document.createElement('li');

        li.innerHTML = i;

        document.querySelector(".year-list").appendChild(li);
    }
}
