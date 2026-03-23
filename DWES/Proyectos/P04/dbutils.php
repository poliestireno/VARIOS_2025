<?php
function conectarDB()
{
    try
    {
        $db = new PDO("mysql:host=localhost;dbname=POLIGONOS","root","");
        $db->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
        return $db;
    }
    catch (PDOException $ex)
    {
        echo "Error conectando ".$ex->getMessage();
    }
}


function realizarQuery($conexion,$texto,$argumentos = null, $isfetch=false)
{
    try
    {
        $comando = $conexion->prepare($texto);
        $comando->execute($argumentos);
        if ($isfetch) return $comando->fetchAll();
    }
    catch (PDOException $ex)
    {
        echo "Error en realizarQuery ".$ex->getMessage();
    }
}

?>