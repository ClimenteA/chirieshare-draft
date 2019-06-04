"use strict";

//Carousel functions
document.addEventListener('DOMContentLoaded', () => {
    let carouselElems = document.querySelector('.carousel.carousel-slider');
    M.Carousel.init(carouselElems, {
            fullWidth: true,
            indicators: false
        });
}, false);


document.getElementById("next").addEventListener("click", () => {
    let elems = document.querySelector('.carousel.carousel-slider');
    let moveRight = M.Carousel.getInstance(elems);
    moveRight.next();
}, false);

document.getElementById("prev").addEventListener("click", () => {
    let elems = document.querySelector('.carousel.carousel-slider');
    let moveLeft = M.Carousel.getInstance(elems);
    moveLeft.prev();
}, false);


// Split facilitati into individual chips
document.addEventListener('DOMContentLoaded', () => {

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

}, false);


//COPY TO CLIPBOARD

var clipboard = new ClipboardJS('.btn');

clipboard.on('success', () => {
    M.toast({html: 'Copiat!'});
});

clipboard.on('error', (e) => {
    M.toast({html: 'Copiere nereusita!'});
});



function joinLaShare() {
    // Adauga-ma la share

    let id_anunt = document.location.pathname.split("/")["2"];
    
    m.request({
        method: "GET",
        url: `/anunturi/join-sheriasi/${id_anunt}`,
    }).then((response) => {
        console.log(response);
        Sheriasi();
        document.getElementById("colegideshare").getElementsByTagName("button")[0].remove();
        createRemoveMeBtn(response);
    });
};


function removeLaShare() {
    // Scoate-ma de la share
        
    let id_anunt = document.location.pathname.split("/")["2"];
    
    m.request({
        method: "GET",
        url: `/anunturi/remove-sheriasi/${id_anunt}`,
    }).then((response) => {
        console.log(response);
        Sheriasi();
        document.getElementById("colegideshare").getElementsByTagName("button")[0].remove();
    });
};



function createAddMeBtn(response){
    // Creaaza colegi de share chips
    
    let root = document.getElementById("colegideshare");

    if (!(response.current_user_added)) {
    // <button class="btn-floating btn waves-effect waves-light green tooltipped" data-position="top" data-tooltip="click pe button daca ai vrea sa imparti chiria pentru acest imobil"><i class="material-icons">add</i></button>
    const Add = {
        view: () => {
            return m('button', {onclick: () => {
                joinLaShare();
            }, "class":"btn-floating btn waves-effect waves-light green add-rem-btn",
                "title":"vreau sa impart chiria pentru acest imobil cu alti colegi"
                }, [
                    m("i", {"class": "material-icons"}, "add")
                ])
        }
    };

    m.mount(root, Add);

}

};


function createRemoveMeBtn(response){
    
    let root = document.getElementById("colegideshare");

    if (response.current_user_added) {
    // <button class="btn-floating btn waves-effect waves-light green tooltipped" data-position="top" data-tooltip="click pe button daca ai vrea sa imparti chiria pentru acest imobil"><i class="material-icons">add</i></button>
    const Remove = {
        view: () => {
            return m('button', {onclick: () => {
                removeLaShare();
            }, "class":"btn-floating btn waves-effect waves-light red lighten-1 add-rem-btn",
                "title":"scoate-ma de la share!"
                }, [
                    m("i", {"class": "material-icons"}, "remove")
                ])
        }
    };

    m.mount(root, Remove);    

}

};


function makeSheriasidiv(){
    
    let sheriasi_exists = document.body.contains(document.getElementById("sheriasi"));

    if (!(sheriasi_exists)){
        let container_sheriasi = document.createElement('div');
        container_sheriasi.setAttribute("id", "sheriasi");
        document.querySelector("div.card:nth-child(4) > div:nth-child(1)").appendChild(container_sheriasi);
    }

};


function Sheriasi(){

    let id_anunt = document.location.pathname.split("/")["2"];

    m.request({
        method: "GET",
        url: `/anunturi/sheriasi/${id_anunt}`,
    }).then((response) => {
        
        console.log(response);

        document.getElementById("colegideshare").classList = [];

        // <a href="#contact-info"><div class="chip blue-grey darken-2 white-text"><img src="http://placeskull.com/100/100/4caf50">Cosmin Tana</div></a> 
        let urlroot = document.baseURI.replace(document.location.pathname, "/cont/utilizator/");
        let id_anunt = document.location.pathname.split("/")["2"];
        let colegideshare = response.colegideshare;

        const Sherias = {
            view: () => {
                return m("div", 
                    colegideshare.map((u) => { return m("a", {href: String(urlroot + u.id + "/" + id_anunt)}, [
                            m("div", {class: "chip blue-grey darken-2 white-text"}, [
                                m("img", {src: (u.imagine != "") ? u.imagine : "http://placeskull.com/100/100/4caf50"}),
                                m("span", (u.first_name != "") ? u.first_name : u.email.split('@')[0])
                            ])
                        ])

                    })
                )
            }
        };

        const Nouser = {
            view: () => {
                return m("h6", "Fi primul la share! Apasa buttonul din dreapta jos!")
            }
        };


        if (response.status === 200 & response.current_user_added == false) {
            // are sheriasi, userul curent nu este adaugat
            createAddMeBtn(response);
            makeSheriasidiv();
            m.mount(document.getElementById("sheriasi"), Sherias);
        }

        else if (response.status === 204 & response.current_user_added == false) {
            // nu are sheriasi, userul curent nu este adaugat
            createAddMeBtn(response);
            makeSheriasidiv();
            m.mount(document.getElementById("sheriasi"), Nouser);
        }

        else if (response.status == 200 & response.current_user_added) {
            // are sheriasi, userul curent este adaugat
            makeSheriasidiv();
            m.mount(document.getElementById("sheriasi"), Sherias);
            createRemoveMeBtn(response);
        }

        else {
            console.log("eroare colegi de share");
        }

    });

};


document.addEventListener("DOMContentLoaded", Sheriasi, false);

