
const tx_usuario = document.getElementById("tx-usuario");
const paragrafo_erro = document.getElementById("paragrafo-erro");


tx_usuario.addEventListener("change", function() {
	let usuario = tx_usuario.value;

	fetch("/existe?usuario=" + usuario).then(function(resposta) {
		return resposta.json()
	}).then(function (json){
		paragrafo_erro.textContent = json.mensagem;
	}).catch(function (){
		paragrafo_erro.textContent = "Erro ao verificar usuário";
	});
});
