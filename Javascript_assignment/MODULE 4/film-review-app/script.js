"use strict";

//submit the form
// const getDataFromForm = ()

// return searchResult
const PICNOTFOUNDURL = "https://via.placeholder.com/210x295?text=Not%20Found";

let filmList = [];
const getDataFromAPI = async (query) => {
  try {
    const response = await fetch(
      `https://api.tvmaze.com/search/shows?${query.name}=${query.value}`
    ); //fetch response from request
    const jsonData = await response.json();
    // const value = jsonData[1];
    return jsonData;
  } catch (error) {
    // handle error
    console.log(error.message);
  }
};

const displayData = (shows) => {
  const result = document.querySelector("#result");
  result.innerHTML = "";
  console.log(shows);
  for (const show of shows) {
    // required information: Name, link to details (url), medium image and summary
    const name = show.show.name;
    const url = show.show.url;
    // const image = show.show.image?.medium; // optional chain
    const image = show.show.image; // image not not show
    const summary = show.show.summary;
    const article = document.createElement("article");
    const h2 = document.createElement("h2");
    const p = document.createElement("p");
    const a = document.createElement("a");
    const img = document.createElement("img");
    const div = document.createElement("div");

    h2.innerText = name;

    a.target = "_blank";
    a.href = url;
    a.innerText = "Link to details";

    img.src = image ? image.medium : PICNOTFOUNDURL;
    img.alt = name;

    div.innerHTML = summary;

    p.appendChild(a);

    article.appendChild(h2);
    article.appendChild(img);
    article.appendChild(p);
    article.appendChild(div);
    result.appendChild(article);
  }
  return;
};

// need to add async and await here to handle api call as it is a async process
const handleClick = async (e) => {
  e.preventDefault();
  const query = document.querySelector("input[name=q]");
  const jsonData = await getDataFromAPI(query);
  // console.log(`film list before fetch: ${filmList}`);
  filmList = jsonData;
  // console.log(filmList);
  displayData(filmList);
  // const data = await displayData(jsonData);
  return jsonData;
  // try {
  //   const
  // }
};

// let filmList = [];
const searchForm = document.querySelector("#search-form");
filmList = searchForm.addEventListener("submit", handleClick);
// console.log(filmList);
