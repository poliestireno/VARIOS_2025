<?php

function operacion3Ref($op1, $op2, $op3, $operador, &$resultado)
{
    switch ($operador) {
        case '+':
            $resultado =$op1 + $op2 + $op3;
            break;
        case '*':
            $resultado =$op1 * $op2 * $op3;
            break;
        default:
            $resultado = 0;
            break;
    }
}

$res = 1;

operacion3Ref(1,2,4,"+",$res);

echo "res:".$res;

$c = 0;
$continuar=true;
while ($continuar)
{
    echo ",".$c;
    $c++;
    $continuar = ($c <= 20) && ($c != 13) ;
}

do
{
    echo ",".$c;
}
while ($continuar);

echo '<br/>';

for ($i=20; $i < 40; $i++) {
    echo ",".$i;
}

echo '<br/>';

$c = 0;
$continuar=true;
for ( ;$continuar; ) {
    echo ",".$c;
    $c++;
    $continuar = ($c <= 20) && ($c != 13) ;
}

echo '<br/>';

$i=20;
for (; $i < 40; ) {
    echo ",".$i;
    $i++;
}

echo '<br/>';

$aPies = array (37,38,47,40);

foreach ($aPies as $elemento)
{
    echo ",".$elemento;
}
echo '<br/>';
$aPies = array("Angel"=>34,"Roberto"=>45,"Miguel"=>47);

var_export($aPies);

echo '<br/>';

foreach ($aPies as $nombre => $nPie) {
    echo $nombre ." calza un ". $nPie;
}

echo '<br/>';

$aLoco = array(12,"rana",$aPies,34);

var_export($aLoco);
echo '<br/>';

$nombre = "mario";

if ($nombre=="jose")
{
    $i=0;
}
else
{
    $i=1;
}

echo $i;

echo '<br/>';

$i = ($nombre=="jose")?0:1;

echo $i;

?>