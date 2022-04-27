<?php
$servername='machines-database.cvczlcshulp9.us-east-2.rds.amazonaws.com:3306';
$username="admin";
$password="password";

try
{
    $con = new PDO("mysql:host=$servername;dbname=machines_database",$username,$password);
    $con->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
<<<<<<< HEAD
   // echo 'Database Connected<br>';
}  
=======
    echo 'Database Connected<br>';
}
>>>>>>> c91d0939161406df5119109d9e6395dcacf68580
catch(PDOException $e)
{
    echo '<br>'.$e->getMessage();
}
<<<<<<< HEAD
     
=======

>>>>>>> c91d0939161406df5119109d9e6395dcacf68580
?>
