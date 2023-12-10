'use strict'
const number = parseInt(prompt("Enter your number"))
    let prime = true;

    for (let i = 2; i <= number; i++) {
        if (number % i ===0){
            console.log("This is a prime number")
            prime = false;
            break }
        }
    if (prime) {
        console.log("THis is not a prime number")
    }