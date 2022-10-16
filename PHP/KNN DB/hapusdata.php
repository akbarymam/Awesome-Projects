<?php
require 'koneksi.php';

$sql = $con->query("SELECT * FROM data ORDER BY id DESC");
$numrows = $sql->fetch_assoc();
for ($i = 1; $i <= $numrows['id']; $i++) {
    $con->query("DELETE FROM data WHERE id=$i");
}
header('location:index.php');
