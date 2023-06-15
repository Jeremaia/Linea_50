var modal1 = document.getElementById("myModal-1");
var btn1 = document.getElementById("openModalBtn-1");
var closeBtn1 = document.getElementById("closeBtn-1");

var modal2 = document.getElementById("myModal-2");
var btn2 = document.getElementById("openModalBtn-2");
var closeBtn2 = document.getElementById("closeBtn-2");

var modal3 = document.getElementById("myModal-3");
var btn3 = document.getElementById("openModalBtn-3");
var closeBtn3 = document.getElementById("closeBtn-3");

var modal4 = document.getElementById("myModal-4");
var btn4 = document.getElementById("openModalBtn-4");
var closeBtn4 = document.getElementById("closeBtn-4");

// Abrir

btn1.onclick = function() {
    modal1.style.display = "block"; // Mostrar
}

btn2.onclick = function() {
    modal2.style.display = "block"; // Mostrar
}

btn3.onclick = function() {
    modal3.style.display = "block"; // Mostrar
}

btn4.onclick = function() {
    modal4.style.display = "block"; // Mostrar
}

// Cerrar

closeBtn1.onclick = function() {
    modal1.style.display = "none"; // Esconder
}

closeBtn2.onclick = function() {
    modal2.style.display = "none"; // Esconder
}

closeBtn3.onclick = function() {
    modal3.style.display = "none"; // Esconder
}

closeBtn4.onclick = function() {
    modal4.style.display = "none"; // Esconder
}
  
// Cerrar al clickear afuera   

window.onclick = function(event) {
    if (event.target == modal1) {
        modal1.style.display = "none"; // Esconder al ser clickeado
    }
}

window.onclick = function(event) {
    if (event.target == modal2) {
        modal2.style.display = "none"; // Esconder al ser clickeado
    }
}

window.onclick = function(event) {
    if (event.target == modal3) {
        modal3.style.display = "none"; // Esconder al ser clickeado
    }
}

window.onclick = function(event) {
    if (event.target == modal4) {
        modal4.style.display = "none"; // Esconder al ser clickeado
    }
}