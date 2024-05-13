const objeto = document.getElementById("par2");
objeto.textContent = "Alterei o parágrafo 2 através JS."

// Texto descritivo.
objeto.title = "Texto descritivo criado no JS."

// mudar estilo
objeto.style.backgroundColor = "brown"

objeto.style.display = "inline-block";

const objeto2 = document.getElementsByClassName("importante");

objeto2[0].style.backgroundColor = "brown"
objeto2[0].style.display = "inline-block";

objeto2[1].style.backgroundColor = "brown"
objeto2[1].style.display = "inline-block";

const objeto3 = document.querySelector("div.div4")

const novo_objeto = document.createElement("p");
novo_objeto.textContent = "JS é bem legal!"
novo_objeto.style.color = "blue";

const imagem = document.createElement("img");
imagem.src = "cachorro.avif";
imagem.alt = "Imagem de um cachorro";

objeto3.appendChild(novo_objeto);
objeto3.appendChild(imagem);
