    'use strict'
    let dog = 0;
    const doglist = [];
    while (dog < 6) {
        let Askuser = prompt("What is the dog's name? ")
        doglist.push(Askuser)
        dog += 1
    }
    doglist.reverse()

    for (let i = 0; i<doglist.length; i++) {
        const li = document.createElement('li');

        li.innerHTML = doglist[i];

        document.querySelector('.DOGLIST').appendChild(li);
    }