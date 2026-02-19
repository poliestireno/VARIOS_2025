<?php
/*
Dado un parrafo sacar el mensaje oculto que corresponde con la primera letra de la primera palabra, 
junto a la segunda letra de la segunda palabra, junto con la tercera letra de la tercera palabra, 
y así hasta el final. En cada palabra se aplica el módulo de su tamaño.

la vida mola toda

lila

*/

function descifrar($frase)
{
    $mensaje = "";
    $palabras = explode(" ",$frase);
    $posicionLetra = 0;
    foreach ($palabras as $pal) 
    {
        
        if ($pal === "") continue;

        $tamPalabra = strlen($pal);
        $mensaje = $mensaje . $pal[$posicionLetra % $tamPalabra];
        $posicionLetra++;
    }

    return $mensaje;
}

$mensajeResuelto = descifrar("la vida es bella");
echo "El mensaje resuelto es:".$mensajeResuelto; //liel
?>