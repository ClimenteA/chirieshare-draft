"use-strict";
M.AutoInit();

// Show loading circle while page is loading
document.body.onload = () => {
    document.body.classList.add("grey");
    document.body.classList.add("lighten-5");
    document.body.style.overflow = "auto";
    document.getElementById("loading").className = "grey lighten-5 none";
}

// Back to top button handler
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
   
