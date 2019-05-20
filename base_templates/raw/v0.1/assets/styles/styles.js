// Custom JS on top of Materialize

// Initialize materializecss
M.AutoInit();



// Responsive navbar
try {

    document.addEventListener('DOMContentLoaded', function() {
        var elems = document.querySelectorAll('.sidenav');
        var instances = M.Sidenav.init(elems, {});
    });

} catch (error) {
  console.log("warning: ", error);
}




// Back to top button handler
try {
// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("up").style.display = "block";
  } else {
    document.getElementById("up").style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

document.getElementById("up").addEventListener("click", topFunction);
    

} catch (error) {
  console.log("warning: ", error);
}



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
  console.log("warning: ", error);
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
  console.log("warning: ", error);
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
  console.log("warning: ", error);
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
  console.log("warning: " + error);
}



// Preloader - while loading show animation 
try {

  document.body.className = "hidden";
  document.body.style.overflow = "hidden";
  document.documentElement.scrollTop = 0;

  document.body.onload = function() {
    document.body.className = "grey lighten-5 body";
    document.body.style.overflow = "auto";
    document.getElementById("loading").className = "grey lighten-5 none";
  }

} catch (error) {
  console.log("warning: " + error);
}



// Carousel image handler

try {

  var carousel = document.getElementsByClassName("image-carousel")[0];
  var controls = document.getElementsByClassName("controls")[0].children;

  var prev = controls[0];
  var next = controls[1];

  function carouselImgState(){    
      var images = document.querySelectorAll("img.none, img.block");
      var img_clases = [];
      for (var i = 0; i < images.length; i++) {
          img_clases.push(images[i].className);
      }
      return {"images":images, "clases": img_clases}
  }


  function imgSlider(fwd=true){
      // Carousel images
      var img_object = carouselImgState();
      console.log(img_object["clases"]);
      for (var i=0; i < img_object["clases"].length; i++) {
          if (img_object["clases"][i] == "block") {
              var array = img_object["images"];
              var len = array.length;
              var current_index = array[i];
              var previous_index = array[(i+len-1)%len];
              var next_index = array[(i+1)%len];
              current_index.className = "none";
              if (fwd){
                  next_index.className = "block";
              }else{
                  previous_index.className = "block";
              };
          }
      }
  }

  function showNext(){imgSlider(true);}
  function showPrevious(){imgSlider(false);}
  
  next.addEventListener("click",  showNext, false);
  prev.addEventListener("click", showPrevious, false);

} catch (error) {
  console.log("warning: " + error);
}


// Modify user interese section

try {

let interese = document.getElementById("interese");
let content = document.getElementById("interese-content");
let field = document.getElementById("interese-field");

interese.addEventListener("click", function(){
  let icontext = String(interese.innerText);

  if (icontext.includes("create")){
  interese.innerText = "check";
  interese.setAttribute("title", "aplica")
  content.className = "white-text none";
  field.className = "input-field block";
  let interese_text = document.getElementById("interese-text");
  interese_text.value = String(content.innerText).trim();
 
  } else if (icontext.includes("check")){
    interese.innerText = "create";
    interese.setAttribute("title", "modifica")
    content.className = "white-text block";
    field.className = "input-field none";
    console.log(document.getElementById("interese-text").value);
    content.innerText = document.getElementById("interese-text").value;

  }

}, false);


} catch (error) {
  console.log("warning: " + error);
}



// Modify user postate section

try {

  let postate = document.getElementById("postate");
  let postate_content = document.getElementById("postate-content");

  postate.addEventListener("click", function(){
    let icontext = String(postate.innerText);
    let postate_list = postate_content.getElementsByTagName("li");

    if (icontext.includes("create")){
        postate.innerText = "check";
        postate.setAttribute("title", "aplica")
        for (let i=0; i < postate_list.length; i++){
          let post_btn = postate_list[i].getElementsByTagName("button")[0];
          post_btn.classList.remove("none");
        }

    } else if (icontext.includes("check")){
        postate.innerText = "create";
        postate.setAttribute("title", "modifica")
        for (let i=0; i < postate_list.length; i++){
          let post_btn = postate_list[i].getElementsByTagName("button")[0];
          post_btn.classList.add("none");
        }
    }

  }, false);
  
} catch (error) {
  console.log("warning: " + error);
}



// Change delete button content on click

try {
  let btnxs_list = document.getElementsByClassName("btn-xs");

  for (let i=0; i < btnxs_list.length; i++){
    btnxs_list[i].addEventListener("click", function(){

      if (btnxs_list[i].innerText.includes("X")){
        btnxs_list[i].innerText = "DE STERS";
      }else if(btnxs_list[i].innerText.includes("DE STERS")){
        btnxs_list[i].innerText = "X";
      }
      
    }, false);
  }
} catch (error) {
  console.log("warning: " + error);
}



// Apply changes

// try {

var apply_icons = document.getElementsByTagName("i");

for (let i=0; i < apply_icons.length; i++){
  console.log(apply_icons[i])
  if (apply_icons[i].getAttribute("title").includes("aplica")){
    console.log("Applying changes..");

  }
}

  
  
// } catch (error) {
//   console.log("warning: " + error);
// }