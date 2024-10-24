<?php

include_once('arquivo_conexao_com_BD.php');

echo "<h1>Conexão com o MongoDB bem-sucedida!</h1>";

// MongoDB\Driver\Query()        <-  Função em PHP que constroe a query
//  [],                          <-  Filtros de busca, neste exemplo nenhum   
//  ['sort' => [ 'nome' => 1],   <-  Definimos a ordenação com o comando ‘sort’ utilizando o atríbuto ‘nome’ e a ordem crescente (1). 
//  'limit' => 5         		 <-  Limitação da quantidade dos resultados apresentado, no exemplo 5 
//  ]);                          <-  Fim da função
$query = new MongoDB\Driver\Query([], ['sort' => [ 'nome' => 1],'limit' => 5]);

$resultado = $conn->executeQuery('classedp.alunos', $query);

echo 'Lista dos Alunos: <br>';

?>

<table border=1><tr>
    <td>Nome</td>
    <td>Turma</td>
</tr>

<?php
// Iterando sobre os resultados e imprimindo os dados
foreach ($resultado as $aluno) {
    echo "<tr><td>$aluno->nome</td><td>$aluno->turma</td></tr>";

}

?>
</table>