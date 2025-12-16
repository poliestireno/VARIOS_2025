<?php

function bigfoot($numeroPie)
{
    return $numeroPie>45;
}

$aPies = array(36,46,37,28,48);

$aPiesGrandes = array_filter($aPies,"bigfoot");

var_export($aPiesGrandes);

?>