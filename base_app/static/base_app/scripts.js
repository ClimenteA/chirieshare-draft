// Specific scripts for current app
"use strict";



// Apply a more depth shadow to articles when hovered

try {

var listings = document.querySelectorAll(".listing");

for (var i = 0; i < listings.length; i++) {

    (function(index){
        listings[i].onmouseover = function(){
            listings[index].className = "listing z-depth-3";
        }   
        
        listings[i].onmouseout = function(){
            listings[index].className = "listing z-depth-2";
        }        
        })(i);

}

} catch (error) {
}



// Toggle filters  

try {

var droparrow = document.getElementById("filtertogglearrow");
var droptext = document.getElementById("filtertoggletext");
var filtre = document.getElementById("filtre");

droparrow.addEventListener("click", function(event){
    
    event.preventDefault();

    if (droparrow.innerText == "arrow_drop_down"){
    droparrow.innerText = "arrow_drop_up";
    droptext.innerText = "Ascunde filtrele";
    filtre.className = "container filters grey lighten-5";
    }else if (droparrow.innerText == "arrow_drop_up"){
    droparrow.innerText = "arrow_drop_down";
    droptext.innerText = "Arata filtrele";
    filtre.className = "none";
    }

}, false);


} catch (error) {
}

// Toggle more filters

try {

var more = document.getElementById("morefilters");
var morefilters = document.getElementById("showmorefilters");

more.addEventListener("click", function(){

    if (more.innerText == "MAI MULT"){
    more.innerText = "MAI PUTIN";
    morefilters.className = "row";
    }else if (more.innerText == "MAI PUTIN"){
    more.innerText = "MAI MULT";
    morefilters.className = "row none";
    }

}, false);

} catch (error) {
}

//Toggle favourite
try {

var favs = document.getElementsByClassName("material-icons small fav blue-grey-text text-lighten-2");

for (var i = 0; i < favs.length; i++) {

    (function(index){
        favs[i].onclick = function(){
            if (favs[index].innerText == "favorite_border"){
                favs[index].innerText = "favorite";

            }else if (favs[index].innerText == "favorite"){
                favs[index].innerText = "favorite_border";
            }
        }    
    })(i);

}
    
} catch (error) {

}



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


// Trimite mesaj

try {

let trimite_mesaj = document.getElementById("trimite-mesaj");

trimite_mesaj.addEventListener("click", () => {

    
    
    m.request({
        method: "POST",
        url: "/update-components/",
        data: all_data
    })
    .then((result) => {

    })

}, false);

} catch (error) {
    
}

