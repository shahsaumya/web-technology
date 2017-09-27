<?php 

define('DB_HOST', 'localhost');
define('DB_NAME', 'exp9'); 
define('DB_USER','root'); 
define('DB_PASSWORD',''); 
$link = mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME);

if (!$link) {
    echo "Error: Unable to connect to MySQL." . PHP_EOL;
    echo "Debugging errno: " . mysqli_connect_errno() . PHP_EOL;
    echo "Debugging error: " . mysqli_connect_error() . PHP_EOL;
    exit;
}

/*echo "Success: A proper connection to MySQL was made! The database is great." . PHP_EOL;
echo "Host information: " . mysqli_get_host_info($link) . PHP_EOL;*/


if(isset($_POST['submit'])) 
{
	session_start(); //starting the session for user profile page 
	if(!empty($_POST['userName'])) //checking the 'user' name which is from Sign-In.html, is it empty or have some text 
	{ 		
		$query = mysqli_query($link,"SELECT * FROM users where userName = '$_POST[userName]' AND password = '$_POST[password]'") or die('error');
		$row = mysqli_fetch_array($query) or die('SORRY... YOU ENTERED WRONG ID AND PASSWORD... PLEASE RETRY...');
		echo "SUCCESSFULLY LOGGED IN TO USER PROFILE PAGE..."; 

	}
} 

?>

<html>
<head>
<title>User Login</title>
<link rel="stylesheet" type="text/css" href="styles.css" />
</head>
<body>
<form name="frmUser" method="post" action="">
	<div class="message"></div>
		<table border="0" cellpadding="10" cellspacing="1" width="500" align="center" class="tblLogin">
			<tr class="tableheader">
			<td align="center" colspan="2">Enter Login Details</td>
			</tr>
			<tr class="tablerow">
			<td>
			<input type="text" name="userName" placeholder="User Name" class="login-input"></td>
			</tr>
			<tr class="tablerow">
			<td>
			<input type="password" name="password" placeholder="Password" class="login-input"></td>
			</tr>
			<tr class="tableheader">
			<td align="center" colspan="2"><input type="submit" name="submit" value="Submit" class="btnSubmit"></td>
			</tr>
		</table>
</form>
</body>
</html>