<?php

echo 'Lista dos Alunos: <br>';

$conn = new MongoDB\Driver\Manager('mongodb://admin:senha@localhost:27017/classedp');

echo "Conexão com o MongoDB bem-sucedida!<br><br>";

// MongoDB\Driver\Query()        <-  Função em PHP que constroe a query
//  [],                          <-  Filtros de busca, neste exemplo nenhum   
//  ['sort' => [ 'nome' => 1],   <-  Definimos a ordenação com o comando ‘sort’ utilizando o atríbuto ‘nome’ e a ordem crescente (1). 
//  'limit' => 5         		 <-  Limitação da quantidade dos resultados apresentado, no exemplo 5 
//  ]);                          <-  Fim da função
$query = new MongoDB\Driver\Query([], ['sort' => [ 'nome' => 1],'limit' => 5]);

$resultado = $conn->executeQuery('classedp.alunos', $query);

// Iterando sobre os resultados e imprimindo os dados
foreach ($resultado as $aluno) {
    echo "$aluno->nome - $aluno->turma<br>\n";
}

echo "<br><br>Lista Exibida!";

?>