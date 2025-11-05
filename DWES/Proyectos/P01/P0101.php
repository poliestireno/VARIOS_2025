<?php

//echo "hola mundo!!!";

$miNombre = "Pepito";

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Mi número de la suerte es el <?php echo rand(1,10);?></h1>
    <h2>el nombre es <?php echo $miNombre?></h2>
    <form method="post" action="P0102.php">
        <input name="miNumero" type="text">
        <input name="miNumero2" type="text">
        <input type="submit" value="dame!!!">
    </form>
</body>
</html>

