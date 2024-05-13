const div1 = document.querySelector("div.div1");
const botao = document.getElementById("botao");


// através de função anonima
botao.onclick = function (e) {
    div1.textContent = "Novo texto da Div 1 através do Botão.";
    alert("Você cliclou no botão corrdenada x= " + e.clientX + " y= " + e.clientY);
}


function troca_texto_no_texto() {
    div1.textContent = "Novo texto da Div 1 através do clique no texto.";
}

div1.onclick = troca_texto_no_texto;

function mensagem_tela() {
    alert("Você passou o mouse na Div1!")
}

function troca_texto_passar() {
    div1.textContent = "Novo texto da Div 1 quando passa o mouse.";
}

// div1.onmouseover = troca_texto_no_texto

div1.addEventListener('mouseover', troca_texto_passar);
div1.addEventListener('mouseover', mensagem_tela);

const txt = document.querySelector("#id_nome")
const botao2 = document.getElementById("botao2")

function filtra_caracter(evt) {
    if (evt.key >= '0' && evt.key <= 9) {
        evt.preventDefault();
    }
}

function valida_dado(event) {
    if (txt.value.trim() == "") {
        event.preventDefault();
    }
}

txt.addEventListener("keydown", filtra_caracter);
botao2.addEventListener("click", valida_dado);