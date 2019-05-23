// Specific scripts for current app
"use strict";


// Split facilitati into individual chips

try {

let facilitati = document.getElementById("facilitati").innerText.split(",");
let other_details = document.getElementById("other-details");

for(let i=0; i < facilitati.length; i++){
    
    let div = document.createElement('div');
    div.className += "chip blue-grey darken-2 white-text";
    div.innerText = facilitati[i];
    other_details.appendChild(div);

    // <div class="chip blue-grey darken-2 white-text">{{ anunt.get_tip_imobil_display }}</div>
}

document.getElementById("facilitati").remove();
    
} catch (error) {

}

