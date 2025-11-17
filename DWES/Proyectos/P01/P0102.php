
<?php

var_export($_POST);

$num = $_POST['miNumero'];
$num2 = $_POST['miNumero2'];

define("PI", 3.14159265359); // define la constante PI
const PI2 = 3.14159;


echo $num, " módulo ",$num2," = ",$num%$num2;

if (($num % 2 == 0) and ($num2 % 2 == 0))
{
    echo " los dos números son pares";
}
else
{
    echo " los dos números no son pares";
}


?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>el cuadrado del número <?= $num; ?> es <?php echo ($num*$num)?></p>
    <p>el cubo del número2 es <?php echo ($num2*$num2*$num2)?></p>
    <p>Pi es <?php echo PI?></p>
    <p>Pi2 es <?php echo PI2?></p>


</body>
</html>