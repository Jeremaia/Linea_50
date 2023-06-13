// TODO: Mejorar el codigo de javascript para que abra todos los modales y no solo el primero

// Obtener el modal
var modal = document.getElementById("myModal-1");

// Obtener el boton
var btn = document.getElementById("openModalBtn-1");

// Obtener el cerrar
var closeBtn = modal.querySelector(".close");

// Funcion para abrir
function openModal() {
    modal.style.display = "block";
}

// Funcion para cerrar
function closeModal() {
    modal.style.display = "none";
}

// Listeners
btn.addEventListener("click", openModal);
closeBtn.addEventListener("click", closeModal);

/*  Pruebas para realizar bucle en los modales, y que se abran todos
// Obtener el modal
var modals = [modal1, modal2, modal3, modal4]
for (var i = 0; i < 4; i++) {
    modals = document.getElementById("myModal-" + (i+1));
}

// Obtener el boton
var btns = [btn1, btn2, btn3, btn4]
for (var i = 0; i < 4; i++) {
    btns = document.getElementById("openModalBtn-" + (i+1));
}

// Obtener el cerrar
var closeBtns = [closeBtn1, closeBtn2, closeBtn3, closeBtn4]
for (var i = 0; i < 4; i++) {
    closeBtns[i] = modal.querySelector(".close-" + (i+1));
}

// Funcion para abrir
var openModals = [openModal1, openModal2, openModal3, openModal4]
for (var i = 0; i < 4; i++) {
    openModals[i] = function() {
        modals[i].style.display = "block";
    }
}

// Funcion para cerrar
function closeModal() {
    modal.style.display = "none";
}

// Listeners
for (var i = 0; i < 4; i++) {
    btns[i].addEventListener("click", openModals[i]);
    closeBtns[i].addEventListener("click", closeModal);
}
*/