"use strict";

let el_body = document.getElementsByTagName("body")[0];
el_body.className += " city grey lighten-4";


// Hide mesaje, vizualizari, din sidenav si topnav

let nav = document.getElementById("nav-mobile");

nav.children[1].style.display = "none";
nav.children[2].style.display = "none";
nav.children[3].style.display = "none"; 


let el_ulnav = document.getElementById("snav");

el_ulnav.children[3].style.display = "none";
el_ulnav.children[4].style.display = "none";
el_ulnav.children[5].style.display = "none";
el_ulnav.children[6].style.display = "none";