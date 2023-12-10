"use strict";
const names = ["John", "Paul", "Jones"];

const element = document.querySelector("#target");

// console.log(names);
for (const user of names) {
  // console.log(user);
  const newLi = document.createElement("li");
  newLi.innerHTML = user;
  element.appendChild(newLi);
}
