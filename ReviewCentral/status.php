<?php
$servername = "localhost";
$username = "root";
$password = "root";
$database="reviews";

// Create connection
$conn = new mysqli($servername, $username, $password,$database);
$result = $conn->query("SELECT status from user where user_id=1");
$row = $result->fetch_assoc();
if ($row['status'] ==  'uploaded'){
	echo "Your file is being procesed";
	die();
}
elseif($row['status'] ==  'complete'){
	echo "Your report is ready";

}
else{
	echo "nothing availble";
	die();
}
$file = fopen("/files/ajsdksad.csv","w");

// foreach ($list as $line)
//   {
//   fputcsv($file,explode(',',$line));
//   }
$result = $conn->query("SELECT * from product where user_id=1");
while ($row = $result->fetch_assoc()){
	// echo 's ';
	fputcsv($file,explode(',',$row));
}


fclose($file);

?>