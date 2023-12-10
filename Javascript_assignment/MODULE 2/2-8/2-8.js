    'use strict';
    const array8 = ["Johnny","DeeDee","Joey","Marky"]
    function concat(a) {
        let sentence = '';
        for (let i = 0; i<a.length; i++) {
            sentence += a[i]
        }
        document.body.innerHTML = sentence

    }
    concat(array8);