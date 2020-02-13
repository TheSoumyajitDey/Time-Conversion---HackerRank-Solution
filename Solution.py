2<?php

$db = "Graphe";
$Ip = "192.168.1.9";
$host = "localhost";
$pass = "";
$user = "root";

    

$conn = mysqli_connect($host,$user,$pass,$db);
if($conn){
    // echo "Connection Successful ";

    date_default_timezone_set("Asia/Kolkata");
    $current_date = date('d/m/y');
    $current_time = date('h:i A');
    $check_in_date = date('d');
    $check_in_day = date('l');
    $check_in_week = date('W');
    $check_in_month = date('F');
    $check_in_year = date('Y');
    $idwal = $Ip.'_'.$current_date;
    
    

    $sql = "select * from users where Ip = '$Ip'";
    $run = mysqli_query($conn,$sql);
    $row = mysqli_fetch_array($run);

    $name = $row['Name'];

    
    if($run)
    {
        $query1 = "insert into attendance (user_att_id, user_id, check_in, check_out, total_hours, date, day, week, month, year)
                 values('$idwal', '$Ip', '0', '0', '0', '$check_in_date', '$check_in_day', '$check_in_week', '$check_in_month', '$check_in_year')";
    $set = mysqli_query($conn,$query1);

        echo "<script>alert('Set');</script>";

        if($set){
            $query = "update attendance set check_in = '$current_time' where user_id = '$Ip'
            and date = '$check_in_date' and day = '$check_in_day' and week = '$check_in_week' 
            and month = '$check_in_month' and year = '$check_in_year'";
        
            mysqli_query($conn,$query);
            }
            else {
                echo "Something is wrong";
            }
    }

    // $array = array($current_date,$current_time,$name);

    // $val = json_encode($array);
    // // print_r($array);
    // echo $val;

    
    





}else {
    echo 'Problem with Connection';
}

?>
