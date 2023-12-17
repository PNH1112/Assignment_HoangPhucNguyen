'use strict';

const form = document.querySelector('form');
const div = document.querySelector('#results');
form.addEventListener('submit', async function (evt) {
    evt.preventDefault(); // Corrected prevention of default form submission
    try {
        const value_from_input = document.querySelector('#query').value;
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${value_from_input}`);
        const jsonData = await response.json();
        div.innerHTML = '';
        for (let data of jsonData) {
            const h2 = document.createElement('h2');
            const a = document.createElement('a');
            const img = document.createElement('img');
            const divElement = document.createElement('div'); // Renamed to avoid conflict
            const article = document.createElement('article');
            h2.innerHTML = data.show.name;
            a.href = data.show.url;
            a.target = "_blank";
            img.src = data.show.image ? data.show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
            divElement.innerHTML = data.show.summary;
            article.appendChild(h2);
            article.appendChild(a);
            article.appendChild(img);
            article.appendChild(divElement);
            div.appendChild(article);
        }
    } catch (error) {
        console.log(error.message);
    }
});