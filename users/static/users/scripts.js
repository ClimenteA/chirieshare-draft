"use strict";

document.addEventListener("DOMContentLoaded", () => {

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


//COPY TO CLIPBOARD

var clipboard = new ClipboardJS('.btn');

clipboard.on('success', () => {
    M.toast({html: 'Copiat!'});
});

clipboard.on('error', () => {
    M.toast({html: 'Copiere nereusita!'});
});



// Send message to poster

document.getElementById("mesaj_client").focus(); 

document.getElementById("mesaj_client").addEventListener("keyup", (event) => {
    
    // On enter key pressed
    if (event.keyCode === 13) {
        event.preventDefault();

        let mesaj = document.getElementById("mesaj_client");
        // let id_anunt = document.location.pathname.split("/")["2"];
        let data = {"mesaj": mesaj.value, "id_anunt": '{{ id_anunt }}'}
        
        if (data.mesaj != ""){

            mesaj.value = "";

            // console.log("Sent: ", data);
            
            m.request({
                method: "GET",
                url: "/anunturi/chirias/",
                data: data
            }).then((response) => {
                if (response.status === 200) {
                    M.toast({html: 'Mesajul a fost trimis!'});
                }else {
                    M.toast({html: 'Mesajul nu a fost trimis!', classes:"red lighten-1"});
                }
            });

        }else {
            M.toast({html: 'Nu ai scris nimic!'});
        }

    }

}, false);






























// END
}, false);



