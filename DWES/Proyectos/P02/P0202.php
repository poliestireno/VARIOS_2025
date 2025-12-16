<?php
var_export($_POST);

$n=$_POST['n'];
echo "<br/>";
for ($i=1; $i <=$n ; $i++)
{
    for ($j=0; $j < $n-$i; $j++)
    {
        echo "_";
    }
    for ($j=0; $j < ($i*2)-1; $j++)
    {
        echo "*";
    }
    echo "<br/>";
}

?>