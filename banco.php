<?php

$servidor = 'localhost';
$usuario = 'root';
$senha = '';
$banco = 'test';
$conn = mysqli_connect($servidor,$usuario,$senha,$banco);

if (!$conn) {
	echo "Não conectado com o Banco";
}else{
	echo "conectado";
}


?>

<?php

$nome = "Joao";
$telefone = "1484";

$sql = "INSERT INTO bot (nome,telefone) VALUES ('$nome','$telefone')";
$query = mysqli_query($conn,$sql);

if (!$query) {
		echo "erro ao inserir";
	}else{
		echo "Deu certo";
	}	

?>