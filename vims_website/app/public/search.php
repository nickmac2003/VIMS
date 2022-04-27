<?php
// Check if the user is already logged in, if yes then redirect them to the search page
if(!isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
    header("location: index.php");
    exit;
}

include 'connect_db.php';
$searchErr = '';
$searchErr2 = '';
$inventory_results='';
if(isset($_GET['save'])) {
    if(!empty($_GET['search'])) {
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
    else {
        $searchErr = "Please Enter a Six Digit Machine ID";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
<title>Search Page</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- Optional theme -->
<link rel="stylesheet" type="text/css" href="static/style.css">
<style>
td {
  text-align: center;
}

table, th, td {
  border: 1px solid;
}

table {
  border-collapse: collapse;
}

th, td {
  padding: 5px;
}

</style>
</head>
<body>
    <div id="id01" class="modal">
    	<form class="modal-content animate" >
        	<div class="imgcontainer">
            		<img src="images/vims.PNG" alt="logo" class="logo">
        	</div>
		<div class="container">
			<br/><br/>
			<form class="form-horizontal" action="#" method="get">	
    			<div class="row" style="margin-top: -40px">
        			<div class="form-group">
            				<label class="control-label col-sm-4" form="machine_id"><b>Machine ID :</b></label>
            				<div class="col-sm-4">
              					<input type="text" class="form-control" name="search" pattern="[0-9]{6}" placeholder="Enter a Six-Digit Machine ID">
           				 </div>
           				 <div class="col-sm-2">
              					<button type="submit" name="save" class="btn btn-success btn-sm">Submit</button>
              					<button type="button" onclick="location.href='VIMS-Map.html'" class="cancelbtn">Map</button>
           				 </div>
        			</div>
        			<div class="form-group">
            				<span class="error" style="color:red;"> <?php echo $searchErr;?> </span>
       				</div>
   			</div>
    			</form>
    			<br/><br/>
			    <h3 style="margin-top: -20px"><u>Machine Information:</u></h3><br/>
   			<div class="table-responsive">
      				<table class="table" style="font-size: 14px">
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
                 			if(!$inventory_results) {
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
				<table class="table" style="font-size: 14px" >
        			<thead>
          				<tr>
            					<th>Machine Total</th>
          				</tr>
        			</thead>
        			<tbody>
					<?php
                 			if(!$cash_in_machine) {
                    			echo '<tr>No data found</tr>';
                 			}
                 			else{
                    				foreach($cash_in_machine as $key=>$value)
                    			{
                        		?>
                    			<tr>
                        			<td><?php echo "$".$value['machine_total'];?></td>
                    			</tr>
                        		<?php
                    			}
                 			}
                			?>
        			</tbody>
				</table>
				</br>
				<table class="table" style="font-size: 14px" >
        			<thead>
          				<tr>
            					<th>Maintenance Date</th>
          				</tr>
        			</thead>
        			<tbody>
				<?php
                		if(!$maintenance_date) {
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
        </form>
    </div>
</body>
</html>
