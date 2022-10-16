<?php
require 'koneksi.php';
require 'config.php';
$data1 = $con->query("SELECT * FROM data ORDER BY id DESC");
$data = $data1->fetch_array();
$tes = $con->query("SELECT * FROM sementara");
$tes1 = $tes->fetch_assoc();
$n = $con->query("SELECT * FROM hitung");
$m = $n->fetch_assoc();
$s = $con->query("SELECT * FROM tb_status");
$d = $s->fetch_assoc();

include 'header.php';

?>

<h2>DATASET</h2>

<?= (empty($data)) ? '<a href="tambah.php" class="btn btn-primary">Tambah Data</a>' : '<a href="hapusdata.php" class="btn btn-danger">Hapus Dataset</a>'; ?>
<hr>
<table border="1" class="table table-hover table-bordered">
    <thead class="table-danger">
        <tr>
            <th scope="col">No</th>
            <th class="text-center" scope="col">X</th>
            <th class="text-center" scope="col">Y</th>
            <th class="text-center" scope="col">Status</th>
        </tr>
    </thead>
    <tbody class="table-dark">
        <?php if ($data == null) {
        ?>
            <tr>
                <th colspan="4" class="text-center">Data Tidak Ada</th>
            </tr>
            <?php
        } else {
            $i = 1;
            foreach ($data1 as $key) {
            ?>
                <tr>
                    <td class="text-center" width='10'><?= $i++; ?></td>
                    <td class="text-center"><?= $key['x']; ?></td>
                    <td class="text-center"><?= $key['y']; ?></td>
                    <td class="text-center"><?= $key['status']; ?></td>
                </tr>
        <?php
            }
        }
        ?>
    </tbody>
</table>
<?php if ($data != null) {
?>
    <form action="config.php" method="post">
        <div class="mb-4 row">
            <label for="k" class="col-sm-1 col-form-label">K :</label>
            <div class="col-sm-2">
                <input type="text" <?= (empty($tes1)) ? '' : 'disabled'; ?> class="form-control" value="<?= (empty($m)) ? '' : $m['k']; ?>" required name="k" id="k">
            </div>
            <label for="x" class="col-sm-1 col-form-label">X :</label>
            <div class="col-sm-2">
                <input type="text" <?= (empty($tes1)) ? '' : 'disabled'; ?> class="form-control" value="<?= (empty($m)) ? '' : $m['x']; ?>" required name="x" id="x">
            </div>
            <label for="y" class="col-sm-1 col-form-label">Y :</label>
            <div class="col-sm-2">
                <input type="text" <?= (empty($tes1)) ? '' : 'disabled'; ?> value="<?= (empty($m)) ? '' : $m['y']; ?>" class="form-control" required name="y" id="y">
            </div>
            <label for="status" class="col-sm-1 col-form-label">Status</label>
            <div class="col-sm-2 ">
                <input type="text" class="form-control" disabled value=" <?= (empty($d)) ? '?' : $d['status']; ?>">
            </div>
        </div>
        <div class="col">
            <button type="submit" <?= (empty($tes1)) ? '' : 'disabled'; ?> name="submit" class="btn me-2 <?= (empty($tes1)) ? 'btn-success' : 'btn-danger'; ?>">Hitung</button>
            <?= (isset($tes1)) ? '<a href="reset.php" class="btn btn-secondary">Reset</a>' : ''; ?>
        </div>
    </form>
    <hr>
    <?php
    $hasil = $con->query("SELECT * FROM sementara");
    $hasil1 = $hasil->fetch_array();
    $input = $con->query("SELECT * FROM hitung");
    $input1 = $input->fetch_assoc();
    if (isset($hasil1)) {
    ?>
        <h2 class="text-center">Jarak</h2>
        <hr>
        <table border="1" class="table mt-3 table-hover table-bordered">
            <thead class="table-warning">
                <tr>
                    <th scope="col">No</th>
                    <th class="text-center" scope="col">X</th>
                    <th class="text-center" scope="col">Y</th>
                    <th class="text-center" scope="col">ED(<?= $input1['x'] . "," . $input1['y']; ?>)</th>
                    <th class="text-center" scope="col">Status</th>
                </tr>
            </thead>
            <tbody class="table-dark">
                <?php if ($hasil == null) {
                ?>
                    <tr>
                        <th colspan="4" class="text-center">Data Tidak Ada</th>
                    </tr>
                    <?php
                } else {
                    $i = 1;
                    foreach ($hasil as $key) {
                    ?>
                        <tr>
                            <td class="text-center" width='10'><?= $i; ?></td>
                            <td class="text-center"><?= $key['x']; ?></td>
                            <td class="text-center"><?= $key['y']; ?></td>
                            <td class="text-center"><?= $key['jarak']; ?></td>
                            <td class="text-center"><?= $key['status']; ?></td>
                        </tr>
                <?php

                        $i++;
                    }
                }
                ?>
            </tbody>
        </table>
    <?php
    }
    ?>
    <?php
    $jarak = $con->query("SELECT * FROM urut");
    $jarak1 = $jarak->fetch_array();
    if (isset($jarak1)) {
    ?>
        <hr>
        <h2 class="text-center">Urut</h2>
        <hr>
        <h4>Data yang Termasuk KNN</h4>
        <h4>Nilai K Adalah Sebesar : <?= $input1['k']; ?></h4>
        <table border="1" class="table mt-3 table-hover table-bordered">
            <thead class="table-primary">
                <tr>
                    <th scope="col">No</th>
                    <th class="text-center" scope="col">X</th>
                    <th class="text-center" scope="col">Y</th>
                    <th class="text-center" scope="col">Status</th>
                    <th class="text-center" scope="col">Jarak</th>
                </tr>
            </thead>
            <tbody class="table-dark">
                <?php
                $i = 1;
                foreach ($jarak as $key) {
                ?>
                    <tr>
                        <td class="text-center" width='10'><?= $i++; ?></td>
                        <td class="text-center"><?= $key['x']; ?></td>
                        <td class="text-center"><?= $key['y']; ?></td>
                        <td class="text-center"><?= $key['status']; ?></td>
                        <td class="text-center"><?= $key['jarak']; ?></td>
                    </tr>
                <?php }
                ?>
            </tbody>
        </table>
    <?php
    }
    $status = $con->query("SELECT * FROM tb_status");
    $status1 = $status->fetch_row();
    ?>
    <?php if ($hasil1 != null) {
        echo "<h4 class='text-center py-2 my-3 bg-info'>
        Terklasifikasi sebagai
        " . $status1[1] . ", dengan X " . $input1['x'] . " dan Y " . $input1['y'] . "
    </h4>";
    } ?>
<?php
} else {
    echo '';
} ?>
<?php include 'footer.php'; ?>