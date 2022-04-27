<?php 

/* Database credentials*/ 
$servername = "authentication-database.cvczlcshulp9.us-east-2.rds.amazonaws.com";
$username = "admin";
$password = "password";
$dbname = "authentication_database";

$con = new mysqli($servername, $username, $password, $dbname);
if ($con->connect_error) {
    die("Connection failed: " . $con->connect_error);
}
//echo "Connected Successfully";

//$con->close();

?>

