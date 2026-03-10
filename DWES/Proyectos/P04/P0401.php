<?php
require_once("dbutils.php");

$miConexion = conectarDB();

//var_export($miConexion);

$aTodosLasPersonas = realizarQuery($miConexion,"SELECT * FROM PERSONAS",null,true);

$aTodosLosCuadrados = realizarQuery($miConexion,"SELECT * FROM CUADRADOS",null,true);

//var_export($aTodosLasPersonas);

$aArgumentosBego = array(":ID_PERSONA"=>"1");
$aCuadradosDeBego = realizarQuery($miConexion,"SELECT * FROM CUADRADOS WHERE ID_PERSONA=:ID_PERSONA",$aArgumentosBego,true);

//var_export($aCuadradosDeBego);




?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>TODOS LOS CUADRADOS</h1>
        <table border="1px">
            <tr><td>NOMBRE</td><td>LADO</td><td>COLOR</td><td>PERSONA</td></tr>
            <?php
                foreach ($aTodosLosCuadrados as $filaI) 
                {
                    $aArgumentosPersona = array(":ID"=>$filaI["ID_PERSONA"]);
                    $aPersonaFromId = realizarQuery($miConexion,"SELECT * FROM PERSONAS WHERE ID=:ID",$aArgumentosPersona,true);
                    echo "<tr>";
                    echo "<td>".$filaI["NOMBRE"]."</td>";
                    echo "<td>".$filaI["LADO"]."</td>";
                    echo "<td>".$filaI["COLOR"]."</td>";
                    echo "<td>".$aPersonaFromId[0]["NOMBRE"]."</td>";
                    echo "</tr>";
                }
            ?>
        </table>
    <h1>LOS CUADRADOS DE BEGO</h1>
        <table border="1px">
            <tr><td>NOMBRE</td><td>LADO</td><td>COLOR</td><td>PERSONA</td></tr>
            <?php
                foreach ($aCuadradosDeBego as $filaI) 
                {
                    $aArgumentosPersona = array(":ID"=>$filaI["ID_PERSONA"]);
                    $aPersonaFromId = realizarQuery($miConexion,"SELECT * FROM PERSONAS WHERE ID=:ID",$aArgumentosPersona,true);
                    echo "<tr>";
                    echo "<td>".$filaI["NOMBRE"]."</td>";
                    echo "<td>".$filaI["LADO"]."</td>";
                    echo "<td>".$filaI["COLOR"]."</td>";
                    echo "<td>".$aPersonaFromId[0]["NOMBRE"]."</td>";
                    echo "</tr>";
                }
            ?>
        </table>
</body>
</html>