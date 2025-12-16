<?php

$aPies = array(36,46,37,28);

var_export ($aPies);

echo "la posición 2 es ".$aPies[1];

$aPersonasPies = array ("ana" => 36, "bego" => 46, "santi"=>37,"pi"=>28);

var_export ($aPersonasPies);

echo "El pie de Santi es ".$aPersonasPies["santi"];

// 1 2 3
// 4 5 6
// 7 8 9

$f1 = array(1,2,3);
$f2 = array(4,5,6);
$f3 = array(7,8,9);
$matriz= array($f1,$f2,$f3);

echo "<br/>";

var_export ($matriz);


for ($i=0; $i < count($aPies); $i++) {
    echo " pie en el índice ".$i." es ". $aPies[$i];
}

foreach ($aPies as $elemento) {
    echo " pie es ". $elemento;
}
$aPersonasPies = array ("ana" => 36, "bego" => 46, "santi"=>37,"pi"=>28);
foreach ($aPersonasPies as $key => $value)
{
    echo " la clave es ".$key;
}

?>