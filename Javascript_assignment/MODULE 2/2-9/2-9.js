    'use strict';
        const normal_array = [1,2,3,4,5,6,7,8];

        function even_number(a) {
            const even_array = [];
            for (let i = 1; i<=a.length; i++) {
                if (i%2===0) {
                    even_array.push(i);
                }

            }
            console.log(even_array);
            console.log(a);
        }

        even_number(normal_array);