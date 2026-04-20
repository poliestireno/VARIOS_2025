<?php


/*
boton para cerrar sesión programaticamente
controlar que se puedan meter en la app1 sin estar LogConfigDataAccessOptions
tiempo de expiración de la sesión
otra pagina de la web app2.php 
*/

session_start();    
require_once("dbutils.php");
echo "POST:";
var_export($_POST);
echo "SESSION:";
var_export($_SESSION);
if (isset($_POST["login_button"]))
{
    $miCon = conectarDB();
    $q= "SELECT * FROM USERS WHERE ALIAS=:ALIAS AND PASS=:PASS";
    $args = array (":ALIAS"=> $_POST['user'],
                    ":PASS"=> md5($_POST['pass'])
                    );
    $results = realizarQuery($miCon, $q,$args,true);
    if ($results)
    {
        echo "login BIEN";
        $_SESSION["user_ok"]=$_POST["user"];
        header("Location: app1.php");
        exit;
    }
    else
    {
        echo "login MAL";
    }

}

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <form action="login.php" method="post">
        <div>user: <input type="text" name="user"></div>
        <div>pass: <input type="password" name="pass"></div>
        <div><input type="submit" name="login_button" value="login"></div>
    </form>
</body>
</html>