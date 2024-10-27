<?php
// incluindo o arquivo de conex�o com o banco de dados
include("arquivo_conexao_com_BD.php");

//obtendo o id da url
$id = $_GET['id'];

// fun��o que transforma o id em um ObjectId para que possa ser utilizado na remo��o
$removerid = new \MongoDB\BSON\ObjectId($id);

// A opera��o BulkWrite � a forma de inserir dados no MongoDB
$bulkWrite=new MongoDB\Driver\BulkWrite;

// informando o id que deve ser removido
$bulkWrite->delete(['_id' => $removerid], array('limit'=>1));

// A fun��o delete gera o formato da query de remo��o e depois deve ser executada no banco e cole��o informados
$conn->executeBulkWrite('classedp.alunos', $bulkWrite);

//redirecionando para a p�gina com a lista dos alunos. No exemplo a index.php
header("Location:index.php");
?>
