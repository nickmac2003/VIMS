<?php
// Include config file
require_once "config.php";

// Define variables and initialize with empty values
$username = $password = "";
$username_err = $password_err = $login_err = "";

// Processing form data when form is submitted
if($_SERVER["REQUEST_METHOD"] == "POST"){

    // Check if username is empty
    if(empty(trim($_POST["username"]))){
        $username_err = "Please enter your username.";
    } else{
        $username = trim($_POST["username"]);
    }

    // Check if password is empty
    if(empty(trim($_POST["password"]))){
        $password_err = "Please enter your password.";
    } else{
        $password = trim($_POST["password"]);
    }

    // Validate credentials
    if(empty($username_err) && empty($password_err)){
        // Prepare a select statement
<<<<<<< HEAD
        $sql = "SELECT id, username, password FROM authentication_database.users WHERE username = ?";
=======
        $sql = "SELECT id, username, password FROM Authentication_Database.users WHERE username =$username ";
>>>>>>> c91d0939161406df5119109d9e6395dcacf68580

        if($stmt = mysqli_prepare($con, $sql)){
            // Bind variables to the prepared statement as parameters
            mysqli_stmt_bind_param($stmt, "s", $param_username);

            // Set parameters
            $param_username = $username;

            // Attempt to execute the prepared statement
            if(mysqli_stmt_execute($stmt)){
                // Store result
                mysqli_stmt_store_result($stmt);

                // Check if username exists, if yes then verify password
                if(mysqli_stmt_num_rows($stmt) == 1){
                    // Bind result variables
		     mysqli_stmt_bind_result($stmt, $id, $username, $password);
                    if(mysqli_stmt_fetch($stmt)){
                        if($_POST['password'] === $password){
                            // Password is correct, so start a new session
                            session_start();

                            // Store data in session variables
                            $_SESSION["loggedin"] = true;
                            $_SESSION["id"] = $id;
                            $_SESSION["username"] = $username;

                            // Redirect user to the search page
                            header("location: search.php");
                        } else{
                            // Password is not valid, display a generic error message
                            $login_err1 = "Invalid Password";
			    echo $login_err1;
                        }
                    }
                } else{
                    // Username doesn't exist, display a generic error message
                    $login_err2 = "Invalid Username";
		    echo $login_err2;
                }
            } else{
                echo "Oops! Something went wrong. Please try again later.";
            }
	     // Close statement
            mysqli_stmt_close($stmt);
        }
    }
        // Close connection
    mysqli_close($con);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VIMS Login</title>
<link rel="stylesheet" type="text/css" href="static/style.css">
</head>
<body>
        <div id="id01" class="modal">

<<<<<<< HEAD
                <form class="modal-content animate" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST">
=======
                <form class="modal-content animate" method="POST" action="search.php">
>>>>>>> c91d0939161406df5119109d9e6395dcacf68580
                        <div class="imgcontainer">

                                <img src="images/vims.PNG" alt="logo" class="logo">
                        </div>
			<div class="container">
                                <label><b>Username</b></label>
                                <input type="text" placeholder="Enter Username" name="username" required>

                                <label><b>Password</b></label>
                                <input type="password" placeholder="Enter Password" name="password" required>

                                <button type="submit">Login</button>
                                <input type="checkbox" checked="checked"> Remember me!
                        </div>

                        <div class="container">
<<<<<<< HEAD
                                <button type="button" onclick="location.href='logout.php'" class="cancelbtn">Clear</button>
=======
                                <button type="button" onclick="location.href='index.php'" class="cancelbtn">Clear</button>
>>>>>>> c91d0939161406df5119109d9e6395dcacf68580
                                <span class="password"></span>
                        </div>
                </form>
        </div>
</body>
</html>
