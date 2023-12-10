    'use strict'
    const DiceNumber = parseInt(prompt("Enter your total dice"));
    const SumOfEye = parseInt(prompt("Enter your sum of dice eyes"));
    const DiceTime = parseInt(prompt("Enter your dice time"));
    let j = 0;
    for (let i = 0; i < DiceTime; i++) {
        let DiceEye = Math.floor(Math.random()*((DiceNumber*6)-1+1)+1);
                    console.log(`No.${i} - ${DiceEye}`)
        if (DiceEye === SumOfEye) {
            j += 1;
            console.log(`***at No.${i} we roll the dice number ${DiceEye} equal to the Sum(${SumOfEye})`)
        }
    }
    let Percent = (j/DiceTime)*100
        Percent = Percent.toFixed(2);
        console.log(`When we roll ${DiceTime} times, the sum of ${DiceNumber} dices (${SumOfEye}) is ${Percent}%`)
