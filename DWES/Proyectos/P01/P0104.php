<?php 
function modulo ($operando,$modulo)
{
    return $operando % $modulo;
}

function esPar($num)
{
    if (modulo($num,2)==0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

function mas3($n)
{
    $n = $n+3;
    return $n;
}
function mas3otra(&$n)
{
    $n = $n+3;
    return $n;
}

echo " la operación del módulo da ".modulo(5,2);

echo " El número 7 es par? ".esPar(7);

var_export(esPar(7));


for ($i=1; $i < 50; $i++) { 
    echo $i;
    var_export(esPar($i));
    echo "<br/>";
}
echo "<br/>";

$miNumerito = 90;
echo " Mi numerito es ".$miNumerito;
mas3($miNumerito);
echo " Mi numerito es ".$miNumerito;
mas3otra($miNumerito);
echo " Mi numerito es ".$miNumerito;

?>