'use strict';
const dice = parseInt(prompt("How many dice do you want?"));
let i = 0;
let sum_dice = 0;

while (i < dice) {
    const number_dice = Math.floor(Math.random() * 6) +1;
    sum_dice += number_dice;
    i += 1;
    console.log(`Roll ${i} time(s): dice is ${number_dice}`);
    console.log(`result is ${sum_dice}`);
}
console.log(`Sum of all roll times: ${sum_dice}`);
