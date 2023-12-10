'use strict';
const askUser = parseInt(prompt("Please enter a number for the dice roll result."))

function rolldice(side) {
    let dice;
    if (askUser > side) {
        alert(`${askUser} is not in range`)
    } else {
        while (dice !== askUser) {
            dice = Math.floor(Math.random() * side) + 1;
            const li = document.createElement('li');
            li.innerHTML = dice;
            document.querySelector(".list_of_roll_dice").appendChild(li);
            console.log(dice);
            }
        }
    }
rolldice(21);