<?php
/*
Dado un array asociativo de 12 elementos, cada uno de ellos clave valor de la temática que se quiera.
Se pide imprimir en html desde php en formato matriz 3x4 en 2 matrices una de claves y otra de valores.
Además se pide con el formato 6x2 (6 filas y 2 columnas)
*/

$letras =
[
    "A" => "1",
    "B" => "2",
    "C" => "3",
    "D" => "4",
    "E" => "5",
    "F" => "6",
    "G" => "7",
    "H" => "8",
    "I" => "9",
    "J" => "10",
    "K" => "11",
    "L" => "12"
];

function escribirMatriz($letras_in,$columnas,$tipo)
{
    $i = 0;
    foreach ($letras_in as $c => $v)
    {
        if ($i % $columnas==0)
        {
            echo "<tr>";
        }
        if ($tipo=="c")
        {
            echo "<td>".$c."</td>";
        }
        else
        {
            echo "<td>".$v."</td>";
        }
        $i++;
        if ($i % $columnas==0)
        {
            echo "</tr>";
        }
    }
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
    <h1>Matriz 3x4 Claves</h1>
    <div>
        <table border="1px">
            <?php
            escribirMatriz($letras,4,"c");
            ?>
        </table>
    </div>
    <h1>Matriz 3x4 Valores</h1>
    <div>
        <table border="1px">
            <?php
            escribirMatriz($letras,4,"v");
            ?>
        </table>
    </div>
    <h1>Matriz 6x2 Claves</h1>
    <div>
        <table border="1px">
            <?php
            escribirMatriz($letras,2,"c");
            ?>
        </table>
    </div>
    <h1>Matriz 6x2 Valores</h1>
    <div>
        <table border="1px">
            <?php
            escribirMatriz($letras,2,"v");
            ?>
        </table>
    </div>
</body>
</html>