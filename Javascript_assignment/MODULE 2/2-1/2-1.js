    'use strict'
    const number_list = [];
    for (let i=1 ; i <=5; i++) {
        let number = parseInt(prompt("Enter your number here"));
        number_list.push(number);
    }
    console.log("Here is numbers of the list")
    for (let j = 4; j>=0; j--) {
        console.log(number_list[j])
    }
