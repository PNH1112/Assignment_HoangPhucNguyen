    'use strict'
    let User;
    const number_list = [];
    while(true) {
        User = parseInt(prompt("Enter your number"));
        if (!number_list.includes(User)) {
        number_list.push(User)}
        else {
            alert("Number has already been given")
            break
        }
    }
    number_list.sort((a,b)=>a-b);
    for (let i = 0; i < number_list.length; i++)
        console.log(number_list[i])