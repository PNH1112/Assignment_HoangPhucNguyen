const changePicture = () => {
  const img = document.querySelector("#target");
  img.src = "img/picB.jpg";
};

const changeBackPicture = () => {
  const img = document.querySelector("#target");
  img.src = "img/picA.jpg";
};

const p = document.querySelector("p");
p.addEventListener("mouseover", changePicture);
p.addEventListener("mouseleave", changeBackPicture);
