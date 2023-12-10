"use strict";
const students = [
  {
    name: "John",
    id: "2345768",
  },
  {
    name: "Paul",
    id: "2134657",
  },
  {
    name: "Jones",
    id: "5423679",
  },
];

const target = document.querySelector("#target");

const addItemToTarget = (obj) => {
  const option = document.createElement("option");
  option.value = `${obj.id}`;
  option.textContent = `${obj.name}`;
  target.appendChild(option);
};

for (let i = 0; i < students.length; i++) {
  addItemToTarget(students[i]);
}

// for (let student of students) {
//   addItemToTarget(student);
// }

// students.forEach((student) => addItemToTarget(student));
