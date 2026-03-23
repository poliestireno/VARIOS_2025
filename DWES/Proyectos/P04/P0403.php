<?php
require_once("dbutils.php");

$miConexion = conectarDB();

//var_export($_POST);
try
{
    $proceso ="EL PROCESO HA IDO BIEN";
    $argumentos= array(":NOMBRE"=>$_POST["NOMBRE"],":APELLIDO"=>$_POST["APELLIDO"],":DESCRIPCION"=>$_POST["DESCRIPCION"]);
    if ($_POST["BOTON"]=="INSERTAR")
    {
        $query = "INSERT INTO PERSONAS (NOMBRE,APELLIDO,DESCRIPCION) values (:NOMBRE,:APELLIDO,:DESCRIPCION)";
        realizarQuery($miConexion,$query,$argumentos,false);
    }
    else if ($_POST["BOTON"]=="ACTUALIZAR POR NOMBRE")
    {
        $query = "UPDATE PERSONAS SET APELLIDO=:APELLIDO,DESCRIPCION=:DESCRIPCION WHERE NOMBRE=:NOMBRE";
        realizarQuery($miConexion,$query,$argumentos,false);
    }
    else if ($_POST["BOTON"]=="BORRAR POR NOMBRE Y APELLIDO")
    {
        $argumentos= array(":NOMBRE"=>$_POST["NOMBRE"],":APELLIDO"=>$_POST["APELLIDO"]);
        $query = "DELETE FROM PERSONAS WHERE NOMBRE=:NOMBRE AND APELLIDO=:APELLIDO";
        realizarQuery($miConexion,$query,$argumentos,false);
    }
}
 catch (Exception $ex)
{
    $proceso ="EL PROCESO HA IDO MAL";
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PROCESOS</title>
</head>
<body>
        <h1><?php echo $proceso?></h1>
        <h1>TODOS LAS PERSONAS</h1>
        <table border="1px">
            <tr><td>NOMBRE</td><td>LADO</td><td>COLOR</td></tr>
            <?php
            $aTodosLasPersonas = realizarQuery($miConexion,"SELECT * FROM PERSONAS",null,true);
                foreach ($aTodosLasPersonas as $filaI) 
                {
                    $aPersonaFromId = realizarQuery($miConexion,"SELECT * FROM PERSONAS",null,true);
                    echo "<tr>";
                    echo "<td>".$filaI["NOMBRE"]."</td>";
                    echo "<td>".$filaI["APELLIDO"]."</td>";
                    echo "<td>".$filaI["DESCRIPCION"]."</td>";
                    echo "</tr>";
                }
            ?>
        </table>
</body>
</html>