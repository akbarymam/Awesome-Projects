<?php
require 'koneksi.php';
$sql = $con->query("SELECT * FROM tb_tambah ORDER BY id DESC");
$numrows = $sql->fetch_assoc();
for ($i = 1; $i <= $numrows['id']; $i++) {
    $con->query("DELETE FROM tb_tambah WHERE id=$i");
}
header('location:tambah.php');
