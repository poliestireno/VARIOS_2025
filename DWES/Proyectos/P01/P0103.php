<?php

$miArr01 = array();

$miArr01[]=12;
$miArr01[]=45;
$miArr01[]="hola";


var_export ($miArr01);

echo " el índice 1 del array tiene el valor ",$miArr01[1];

echo '<br/>';
$miArr02 = ["nombre" => "Juan", "apellido" => "Pérez"];

var_export ($miArr02);

echo " el apellido es ". $miArr02["apellido"];

?>