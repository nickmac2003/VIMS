<?php
$servername='machines-database.cvczlcshulp9.us-east-2.rds.amazonaws.com:3306';
$username="admin";
$password="password";

try
{
    $con = new PDO("mysql:host=$servername;dbname=machines_database",$username,$password);
    $con->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
    echo 'Database Connected<br>';
}
catch(PDOException $e)
{
    echo '<br>'.$e->getMessage();
}

?>
