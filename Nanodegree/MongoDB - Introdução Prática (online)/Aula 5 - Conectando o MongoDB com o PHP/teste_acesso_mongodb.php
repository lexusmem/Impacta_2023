<?php

echo 'Testando a conexão entre o PHP e o MongoDB: <br>';

$conn = new MongoDB\Driver\Manager('mongodb://admin:senha@localhost:27017/classedb');

echo "Conexão com o MongoDB bem-sucedida!<br>";

var_dump($conn->getServers());

echo "<br><br>Bancos de dados:\n";
$listDatabasesCommand = new MongoDB\Driver\Command(['listDatabases' => 1]);
$cursor = $conn->executeCommand('admin', $listDatabasesCommand);
foreach ($cursor as $document) {
    echo "<br><br>";
    var_dump($document);
}

?>