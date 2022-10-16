<?php
require 'koneksi.php';
$sql = $con->query("SELECT * FROM sementara ORDER BY id DESC");
$numrows = $sql->fetch_assoc();
for ($i = 1; $i <= $numrows['id']; $i++) {
    $con->query("DELETE FROM sementara WHERE id=$i");
}
$sql = $con->query("SELECT * FROM urut ORDER BY id DESC");
$numrows = $sql->fetch_assoc();
for ($i = 1; $i <= $numrows['id']; $i++) {
    $con->query("DELETE FROM urut WHERE id=$i");
}
$sql = $con->query("SELECT * FROM tb_status ORDER BY id DESC");
$numrows = $sql->fetch_assoc();
for ($i = 1; $i <= $numrows['id']; $i++) {
    $con->query("DELETE FROM tb_status WHERE id=$i");
}
$sql = $con->query("SELECT * FROM hitung ORDER BY id DESC");
$numrows = $sql->fetch_assoc();
for ($i = 1; $i <= $numrows['id']; $i++) {
    $con->query("DELETE FROM hitung WHERE id=$i");
}
header('location:index.php');
