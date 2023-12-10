        'use strict';
        const name_4 = prompt("Type your name");
        function getRandomInt(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1) + min);
        }
        const randomNum = getRandomInt(1, 4);
        let house;
        if (randomNum === 1) {
            house = "Gryffindor"
            console.log(name_4, " to ", house );
        }
        if (randomNum === 2) {
            house = "Slytherin"
            console.log(name_4, " to ", house);
        }
        if (randomNum ===3) {
            house = "Hufflepuff"
            console.log(name_4, " to ", house);
        }
        if (randomNum === 4) {
            house = "Ravenclaw"
            console.log(name_4, " to ", house);
        }