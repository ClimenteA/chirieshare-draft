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
        if (document.getElementById("modifpass").innerText !== "SCHIMBARE PAROLA") {
            M.toast({html: 'Parolele nu se potrivesc sau nu ai minim 8 caractere!', classes: 'red lighten-1'});
            event.preventDefault();
            passwords[1].value = "";
            passwords[2].value = "";
            passwords[1].focus();
        }
    }
}, false);


// TODO: Resetare parola 

let log_nereusit = document.getElementById("lognereusit");
    
log_nereusit.addEventListener("click", (ev) => {
    ev.preventDefault();
   
    let el_modif = document.getElementById("modifpass");
    el_modif.click();
    el_modif.innerText = "SCHIMBARE PAROLA";
    document.getElementById("pass").innerText = "Codul primit prin email";
    document.getElementById("confpass").innerText = "Parola noua";
    document.getElementById("reg").innerText = "TRIMITE-MI CODUL";
    document.getElementById("reg").onclick = (event) => {
        M.toast({html: 'Ti-am trimis un cod prin email!'});
        event.preventDefault();
        m.request({
            method: "POST",
            action: "/autentificare/resetare/",
        }).then((result) => {
            document.getElementById("reg").innerText = "SCHIMBA PAROLA";
        });
        
    };
}, false);





