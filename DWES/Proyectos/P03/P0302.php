<?php

function por2($n)
{
    return $n*2;
}

$nums = array(4, 3, 1, 5, 2);


$numsPor2 = array_map("por2",$nums);

print_r($numsPor2);


function mul($carry, $item) {
    $carry *= $item;
    return $carry;
}
$mulTotal = array_reduce($numsPor2,"mul",1);
echo "Multiplicación total:".$mulTotal;
$mulTotal2 = array_reduce($nums,"mul",1);
echo "Multiplicación total2:".$mulTotal2;


sort($nums);

print_r($nums);

sort($numsPor2);

print_r($numsPor2);

echo in_array("4",$numsPor2);

echo "hola";

?>