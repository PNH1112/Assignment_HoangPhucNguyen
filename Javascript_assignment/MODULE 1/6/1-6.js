'use strict';
const should = confirm ('Should i calculate the square root?')
if (should) {
    const number_no = prompt("Type your number")
    if (number_no > 0) {
    let sqrt = Math.sqrt(number_no);
    console.log(sqrt);
    }
    else {
        console.log("The square root of a negative number is not defined")}}
else {
    console.log("The square root is not calculated.")
}