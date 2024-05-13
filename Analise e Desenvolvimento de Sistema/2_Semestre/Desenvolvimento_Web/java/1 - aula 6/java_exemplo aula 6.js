alert("Primeiro exemplo em JS");

console.log("Segundo exemplo em JS");

// https://pythontutor.com/javascript.html#mode=edit
/*
Aula executada no python tutor para verificar sintaxe e variáveis
*/
var a = 10;
let b = "JS é muito legal";
const c = 5.3;

a = 20;
b = "JS é fácil"
// variável do tipo const não pode ser alterada
//c = 7.2;

// podemos declarar variável sem valor
let x;
x = 100;

let w = 10;
let y = 10.5;
let z = true;
let p = false;

// saber o tipo de variável - typeof
// imprimir - console.log
console.log(typeof (w));
console.log(typeof (y));
console.log(typeof (z));
console.log(typeof (p));

// declaração valor null/none
let d = null
console.log(typeof (d));

// linguagem fracamente tipada
let f = w + b
console.log(f)

let g = "10"
f = w + g
console.log(f)


// operações aritméticos
a = 10;
w = 2;
f = a + w;
console.log(f);
f = a - w;
console.log(f);
f = a * w;
console.log(f);
f = a / w;
console.log(f);
f = a % w;
console.log(f);

// operações logico
console.log(a == w);
console.log(a != w);
console.log(a > w);
console.log(a < w);
console.log(a >= w);
console.log(a <= w);

/* operador relacionais
&& => and
|| => or
!  => not
*/
g = "10";
a = 10;

console.log(g == a);
console.log(g === a);

// arrays (vetores / listas)
let lista = [1, 3, 5, 7, 9];
let lista_2 = [1, "3", true, 1 > 2, 5.8];
console.log(lista_2);

let lista_vazia = [];

lista_vazia[0] = 1;
lista_vazia[1] = 2;
lista_vazia[2] = 3;
lista_vazia[3] = 4;
lista_vazia[8] = 9;

// método para adicionar no final da lista .push
lista_vazia.push("teste última posição")

// tamanho da lista
console.log(lista_vazia.length);

console.log(lista_vazia);

// remove último item da lista método POP
// Porém é possível já atribuir este valor a uma variável.
let removido = lista_vazia.pop();
console.log(removido);

// objetos (dicionários)

let objeto = { "nome": "Alex", "cpf": 22920975838, "casado": true, "notas": [8, 9, 10] };
// adicionando chaves aos objetos
objeto["cidade"] = "São Paulo";
objeto.empresa = "allseg";
console.log(objeto);
console.log(objeto.nome);
console.log(objeto["cidade"]);
console.log(objeto["notas"][1]);
console.log(objeto.notas[2]);

// declaração de função
function soma(a, b) {
    let c = a + b;
    return c;
};

let resultado = soma(3, 4);
console.log(resultado);


// funções anonimas
const soma_2 = function (a, b) {
    let c = a + b;
    return c;
};

let resultado_2 = soma_2(3, 4);
console.log(resultado_2);

// condicionais
let nota = 7;

if (nota >= 6) {
    console.log("Aprovado");
} else {
    console.log("Reprovado");
}

let frequencia = 80;

if (nota >= 6 && frequencia >= 75) {
    console.log("Aprovado");
} else {
    console.log("Reprovado");
}

nota = 4;
if (nota >= 6) {
    console.log("Aprovado");
} else if (nota >= 3 && nota < 6) {
    console.log("Recuperação");
} else {
    console.log("Reprovado");
}

// estrutura de repetição

let i = 1;

while (i <= 5) {
    console.log(i);
    i++
}

i = 6
do {
    console.log(i);
    i++;
} while (i <= 6);

for (i = 1; i < 5; i++) {
    console.log(i)
}

let nomes = ["alex", "ana", "joão", "pedro"];

for (let n = 0; n < nomes.length; n++) {
    console.log(nomes[n]);
}

for (let nome of nomes) {
    console.log(nome);
}