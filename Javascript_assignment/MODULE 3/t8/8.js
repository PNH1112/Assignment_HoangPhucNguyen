"use strict";

const getValueAB = () => {
  const valueA = document.querySelector("#num1").value;
  const valueB = document.querySelector("#num2").value;
  const operation = document.querySelector("#operation").value;
  return [valueA, valueB, operation];
};

const calculate = (numA, numB, operation) => {
  let result;
  const [intA, intB] = [+numA, +numB];
  switch (operation) {
    case "add":
      result = intA + intB;
      break;
    case "sub":
      result = intA - intB;
      break;
    case "multi":
      result = intA * intB;
      break;
    case "div":
      result = intA / intB;
      break;
  }
  return result;
};

const displayResult = (result) => {
  const target = document.querySelector("#result");
  target.innerHTML = result;
};
const execute = () => {
  const [numA, numB, operation] = getValueAB();
  const result = calculate(numA, numB, operation);
  displayResult(result);
};

const button = document.querySelector("button");
// button;
const result = button.addEventListener("click", execute);
console.log(`this is result: ${result}`);
// document.querySelector("#result").innerHTML = result;
// result;
