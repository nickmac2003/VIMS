<?php
include 'connect_db.php';
$searchErr = '';
$inventory_results='';
if(isset($_GET['save']))
{
    if(!empty($_GET['search']))
    {
        $search = $_REQUEST['search'];
        $stmt = $con->prepare("SELECT * FROM machines_database.inventory where machine_id =$search ");
        $stmt->execute();
        $inventory_results = $stmt->fetchAll(PDO::FETCH_ASSOC);
        //print_r($inventory_results);
		$stmt2 = $con->prepare("SELECT maintenance_date FROM machines_database.machine WHERE machine_id =$search ");
        $stmt2->execute();
        $maintenance_date = $stmt2->fetchAll(PDO::FETCH_ASSOC);
		//print_r($maintenance_date);
		$stmt3 = $con->prepare("SELECT * FROM machines_database.money WHERE machine_id =$search ");
        $stmt3->execute();
        $cash_in_machine = $stmt3->fetchAll(PDO::FETCH_ASSOC);
		//print_r($cash_in_machine);
    }
    else
    {
        $searchErr = "Please enter the information";
    }

}

?>

<html>
<head>
<title>Search Page</title>
<link rel="stylesheet" href="bootstrap.css" crossorigin="anonymous">
<!-- Optional theme -->
<link rel="stylesheet" type="text/css" href="static/style.css">
<style>td {
  text-align: center;
}
table, th, td {
  border: 1px solid;
}
table {
  border-collapse: collapse;
}</style>
</head>
<body>
		<div id="id01" class="modal">
			<form class="modal-content animate" action="search.php">
        <div class="imgcontainer">
            <img src="images/vims.PNG" alt="logo" class="logo">
        </div>
		<div class="container">
			<br/><br/>
			<form class="form-horizontal" action="#" method="get">	
    <div class="row">
        <div class="form-group">
            <label class="control-label col-sm-4" for="email"><b>Machine ID :</b></label>
            <div class="col-sm-4">
              <input type="text" class="form-control" name="search" placeholder="Enter the Six-Digit Machine ID">
            </div>
            <div class="col-sm-2">
              <button type="submit" name="save" class="btn btn-success btn-sm">Submit</button>
              <button type="button" onclick="document.getElementById('id01').style.display='none'" class="cancelbtn">Cancel</button>
            </div>
        </div>
        <div class="form-group">
            <span class="error" style="color:red;"> <?php echo $searchErr;?></span>
        </div>
    </div>
    </form>
    <br/><br/>
    <h3><u>Machine Information:</u></h3><br/>
    <div class="table-responsive">
      <table class="table">
        <thead>
          <tr>
            <th>  Machine ID  </th>
            <th>  Pepsi  </th>
            <th>  Diet Pepsi  </th>
            <th>  Dr Pepper  </th>
            <th>  Mt Dew  </th>
            <th>  Sierra Mist  </th>
          </tr>
        </thead>
        <tbody>
				<?php
                 if(!$inventory_results)
                 {
                    echo '<tr>No data found</tr>';
                 }
                 else{
                    foreach($inventory_results as $key=>$value)
                    {
                        ?>
                    <tr>
                        <td><?php echo $value['machine_id'];?></td>
                        <td><?php echo $value['pe_qty'];?></td>
                        <td><?php echo $value['dp_qty'];?></td>
                        <td><?php echo $value['dr_qty'];?></td>
                        <td><?php echo $value['md_qty'];?></td>
                        <td><?php echo $value['sm_qty'];?></td>
                    </tr>
                        <?php
                    }
                 }
                ?>
        </tbody>
		</table>
		</br>
		<table class="table">
        <thead>
          <tr>
            <th>Fives</th>
			<th>Dollars</th>
			<th>Quarters</th>
            <th>Dimes</th>
            <th>Nickels</th>
            <th>Machine Total</th>
          </tr>
        </thead>
        <tbody>
				<?php
                 if(!$cash_in_machine)
                 {
                    echo '<tr>No data found</tr>';
                 }
                 else{
                    foreach($cash_in_machine as $key=>$value)
                    {
                        ?>
                    <tr>
                        <td><?php echo $value['fives_qty'];?></td>
						<td><?php echo $value['dollars_qty'];?></td>
						<td><?php echo $value['quarters_qty'];?></td>
                        <td><?php echo $value['dimes_qty'];?></td>
                        <td><?php echo $value['nickels_qty'];?></td>
                        <td><?php echo "$".$value['machine_total'];?></td>
                    </tr>
                        <?php
                    }
                 }
                ?>
        </tbody>
		</table>
		</br>
		<table class="table">
        <thead>
          <tr>
            <th>Maintenance Date</th>
          </tr>
        </thead>
        <tbody>
				<?php
                 if(!$maintenance_date)
                 {
                    echo '<tr>No data found</tr>';
                 }
                 else{
                    foreach($maintenance_date as $key=>$value)
                    {
                        ?>
                    <tr>
                        <td><?php echo $value['maintenance_date'];?></td>
                     
                    </tr>
                        <?php
                    }
                 }
                ?>
        </tbody>
		</table>
    </div>
</div>
<script src="jquery-3.2.1.min.js"></script>
<script src="bootstrap.min.js"></script>
</body>
</html>