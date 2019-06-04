




//Toggle favourite

let favs = document.getElementsByClassName("material-icons small fav blue-grey-text text-lighten-2");

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
  