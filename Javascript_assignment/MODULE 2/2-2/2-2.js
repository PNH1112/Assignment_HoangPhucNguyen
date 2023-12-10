    'use strict'
    const Participant = [];
    let AskUser = prompt("Tell me the number of participants");
    while (AskUser !== "") {
        Participant.push(AskUser)
    AskUser = prompt("Tell me the number of participants");

}
    Participant.sort()
    console.log("List of participants:")
    for (let i = 0; i<Participant.length;i++){
        const li = document.createElement('li');

        li.innerHTML = Participant[i];

        document.querySelector(".Participant_list").appendChild(li);
    }