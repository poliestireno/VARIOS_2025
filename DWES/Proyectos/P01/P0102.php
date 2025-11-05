
<?php

var_export($_POST);

$num = $_POST['miNumero'];
$num2 = $_POST['miNumero2'];

?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>el cuadrado del número es <?php echo ($num*$num)?></p>
    <p>el cubo del número2 es <?php echo ($num2*$num2*$num2)?></p>
</body>
</html>