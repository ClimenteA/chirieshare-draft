"use strict";

// Add fav to user list

function handleFavorite(action, fav){

    var id_anunt;
    
    if (document.location.pathname.split("/")["2"] == undefined){
        id_anunt = fav.parentElement.firstElementChild.href.split("/")[4];
    }
    else {
        id_anunt = document.location.pathname.split("/")["2"];
    }
    
    if (action == "add") {
        m.request({
            method: "GET",
            url: `/anunturi/adauga-favorit/${id_anunt}`,
        }).then((response) => {
            // console.log(response);
            M.toast({html: 'Adaugat la favorite!'});
        });

    }

    else if (action == "delete") {
        m.request({
            method: "GET",
            url: `/anunturi/scoate-favorit/${id_anunt}`,
        }).then((response) => {
            // console.log(response);
            M.toast({html: 'Scos de la favorite!'});
        });
    }

};


//Toggle favourite send the request to server

let favs = document.getElementsByClassName("material-icons small fav blue-grey-text text-lighten-2");

for (var i = 0; i < favs.length; i++) {

    (function(index){
        favs[i].onclick = function(){
            if (favs[index].innerText == "favorite_border"){
                favs[index].innerText = "favorite";

                handleFavorite("add", favs[index]);

            }else if (favs[index].innerText == "favorite"){
                favs[index].innerText = "favorite_border";
                
                handleFavorite("delete", favs[index]);

            }
        }    
    })(i);

}
  