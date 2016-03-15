<?php 

if(isset($_POST)){
move_uploaded_file($_FILES["csvfile"]['tmp_name']
, "files/1.csv" );
}
header('Location: status.php');
?>

<!DOCTYPE html>
<html >
  <head>
    <meta charset="UTF-8">
    <title>Review Central</title>

<link rel='stylesheet prefetch' href='http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css'>
<link rel='stylesheet prefetch' href='http://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.0/css/datepicker.css'>
<link rel="stylesheet" href="css/style.css">

 <style type="text/css">
    .btn-file {
    position: relative;
    overflow: hidden;
  }
  
  .btn-file input[type=file] {

      position: absolute;
      top: 0;
      right: 0;
      min-width: 100%;
      min-height: 100%;
      font-size: 100px;
      text-align: right;
      filter: alpha(opacity=0);
      opacity: 0;
      outline: none;
      background: white;
      cursor: inherit;
      display: block;
      text-align: center;
}
    </style>   
        
</head>
<body background="bg.jpg">
<h1><label>Review Central</label></h1>

<form method="post" enctype="multipart/form-data">
<span class="btn btn-default btn-file">
      Input File <input name="csvfile" type="file">
    </span>

<br>
<label>Select start date: </label>
<div id="datepicker" class="input-group date" data-date-format="mm-dd-yyyy">
    <input  class="form-control" type="text" readonly />
    <span class="input-group-addon"><i class="glyphicon glyphicon-calendar"></i></span>
</div>
<input type="submit"/>
</form>

<script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
<script src='http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js'></script>
<script src='http://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.0/js/bootstrap-datepicker.js'></script>
<script src="js/index.js"></script>
    
</body>
</html>
