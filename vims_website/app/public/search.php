<?php
include 'connect_db.php';
$searchErr = '';
$inventory_results='';
if(isset($_POST['save']))
{
    if(!empty($_POST['search']))
    {
        $search = $_POST['search'];
        $stmt = $con->prepare("SELECT * FROM machines_database.inventory where machine_id like '%$search%'");
        $stmt->execute();
        $inventory_results = $stmt->fetchAll(PDO::FETCH_ASSOC);
        //print_r($inventory_results);
         
    }
    else
    {
        $searchErr = "Please enter the information";
    }
    
}
 
?>
<?php
phpinfo();
?>
<html>
<head>
<title>Search Page</title>
<link rel="stylesheet" href="bootstrap.css" crossorigin="anonymous">
<!-- Optional theme -->
<link rel="stylesheet" type="text/css" href="css/style.css">
<style>

</style>
</head>
 
<body>
		<div id="id01" class="modal">
		<form class="modal-content animate" action="/search.php">
			<div class="imgcontainer">
				
				<img src="images/vims.png" alt="logo" class="logo">
			</div>
		<div class="container">
        <br/><br/>
        <form class="form-horizontal" action="#" method="post">
		<div class="row">
        <div class="form-group">
            <label class="control-label col-sm-4" for="email"><b>Machine ID :</b></label>
            <div class="col-sm-4">
              <input type="text" class="form-control" name="search" placeholder="Enter the Six-Digit Machine ID">
            </div>
            <div class="col-sm-2">
              <button type="submit" name="save" class="btn btn-success btn-sm">Submit</button>
            </div>
        </div>
        <div class="form-group">
            <span class="error" style="color:red;"> <?php echo $searchErr;?></span>
        </div>
         
    </div>
    </form>
    <br/><br/>
    <h3><u>Search Result</u></h3><br/>
    <div class="table-responsive">          
      <table class="table">
        <thead>
          <tr>
            <th>Machine ID  |  </th>
            <th>Pepsi  |  </th>
            <th>Diet Pepsi  |  </th>
            <th>Dr Pepper  |  </th>
            <th>Mt Dew  |  </th>
			<th>Sierra Mist</th>
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
                        <td><?php echo $key+1;?></td>
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
    </div>
</div>
<script src="jquery-3.2.1.min.js"></script>
<script src="bootstrap.min.js"></script>
</body>
</html>