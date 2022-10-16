<?php
require 'koneksi.php';
if (isset($_POST['submit'])) {
    $x = $_POST['x'];
    $y = $_POST['y'];
    $k = $_POST['k'];

    $con->query("INSERT INTO hitung VALUES ('','$x','$y','$k')");
    $sql = $con->query("SELECT * FROM data ORDER BY id DESC");
    $numrows = $sql->fetch_array();
    for ($i = 1; $i <= $numrows['id']; $i++) {
        $sql1 = mysqli_query($con, "SELECT * FROM data Where id = $i");
        while ($data = mysqli_fetch_array($sql1)) {
            $v1 = $x - $data['x'];
            $v2 = $y - $data['y'];
            $hit1 = (pow($v1, 2)) + (pow($v2, 2));
            $hit2 = sqrt($hit1);
            $con->query("INSERT INTO sementara VALUES ('$i','$hit2','$data[x]','$data[y]','$data[status]')");
        }
    }
    $sql3 = $con->query("SELECT * FROM  `sementara` ORDER BY  `sementara`.`jarak` ASC LIMIT 0 , $k");
    $x = 1;
    while ($data = $sql3->fetch_array()) {
        $con->query("INSERT INTO urut VALUES ('$x','$data[jarak]','$data[x]','$data[y]',
'$data[status]')");
        $x = $x + 1;
    }
    $sqlr = $con->query("SELECT * FROM  urut ORDER BY id ASC LIMIT 0 , 1");
    while ($datates = $sqlr->fetch_array()) {
        $sqlx = $con->query("SELECT * FROM  urut ORDER BY id ASC");
        while ($datax = $sqlx->fetch_array()) {
            if ($datax['jarak'] == '0') {
                $Status = $datax['status'];
                $x = $datax['x'];
                $y = $datax['y'];
                $con->query("INSERT INTO tb_status VALUES ('','$Status')");
                break;
            } else {
                $Status = $datax['status'];
                $x = $datax['x'];
                $y = $datax['y'];
                $con->query("INSERT INTO tb_status VALUES ('','$Status')");
                break;
            }
        }
    }
    header("location:index.php");
}
