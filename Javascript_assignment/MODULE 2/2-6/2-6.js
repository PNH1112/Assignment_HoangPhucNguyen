    'use strict';
    function rolldice() {
    let dice;
        while (dice !== 6) {
            dice = Math.floor(Math.random() * 6) + 1;
            const li = document.createElement('li');
            li.innerHTML = dice;
            document.querySelector(".list_of_roll_dice").appendChild(li);
            console.log(dice);
            if (dice ===6) {
                break;
            }
        }
    }
    rolldice();