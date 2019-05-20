// Specific JS for users app
"use strict";

let el_body = document.getElementsByTagName("body")[0];
el_body.className += " city grey lighten-4";


let emails = document.querySelectorAll('input[type=email]');
let passwords = document.querySelectorAll('input[type=password]');

emails[0].value = "";
emails[1].value = "";

passwords[0].value = "";
passwords[1].value = "";
passwords[2].value = "";

let register = document.getElementById("reg");

register.addEventListener("click", (event) => {
    if(!(passwords[1].value == passwords[2].value && passwords[1].value.length >= 8  && passwords[2].value.length >= 8)){
        M.toast({html: 'Parolele nu se potrivesc sau nu ai minim 8 caractere!', classes: 'rounded red lighten-1'});
        event.preventDefault();
        passwords[1].value = "";
        passwords[2].value = "";
        passwords[1].focus();
    }
}, false);
    





