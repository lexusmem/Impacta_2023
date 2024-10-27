<html>
<body>
<?php

include_once("arquivo_conexao_com_BD.php");

if(isset($_POST['Submit'])) {
	$user = array ('nome' => $_POST['nome'],'idade' => $_POST['idade'],'turma' => $_POST['turma'],'sexo' => $_POST['sexo'],'nota' => $_POST['nota']);
	
$errorMessage = '';

foreach ($user as $key => $value){
	if (empty($value)) {
		$errorMessage .= $key . ' esta em branco<br/>'; 
	}
}	

if($errorMessage){
	echo '<span style = "color:red">'. $errorMessage ."</span>";
	echo "<br />< href='javascript:self.history.back();'>Voltar</a>";
}	
	else {
		
		$bulk = new MongoDB\Driver\BulkWrite;
		$bulk->insert(['nome' => $user['nome'],'idade' => $user['idade'], 'sexo' => $user['sexo'], 'turma' => $user['turma'], 'nota' => $user['nota']]);
		
		$conn->executeBulkWrite('classedp.alunos', $bulk);
		
		echo "<font color='green'>Aluno inserido com sucesso!</font>";
		echo "<br><a href='index.php'>Listar resultado</a>";
		
	}
}

?>
</body>
</html>