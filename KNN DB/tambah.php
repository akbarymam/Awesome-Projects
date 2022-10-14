<?php require 'koneksi.php';

$ada = $con->query("SELECT * FROM tb_tambah");
$ada1 = $ada->fetch_array();
include 'header.php';
?>
<h2 class="my-3 text-center">Tambah Dataset</h2>
<form method="post">
    <div class="mb-4 row">
        <label for="k" class="col-sm-1 col-form-label">K :</label>
        <div class="col-sm-2">
            <input type="text" value="<?= (empty($ada1)) ? '' : $ada1['k']; ?>" <?= (empty($ada1)) ? '' : 'disabled'; ?> class="form-control" required name="k">
        </div>
        <button type="submit" <?= (empty($ada1)) ? '' : 'disabled'; ?> name="submit" class="btn col-sm-1 ms-3 btn-danger">Hitung</button>
        <a href="resetmbh.php" class="btn col-1 ms-4 btn-secondary">Reset</a>
    </div>
</form>
<form method="post">
    <?php
    if (isset($_POST['submit'])) {
        $ada = 'ada';
        $k = $_POST['k'];
        $con->query("INSERT INTO tb_tambah VALUES ('','$ada','$k')");
        for ($i = 1; $i <= $_POST['k']; $i++) {
    ?>
            <input type="hidden" name="k" value="<?= $_POST['k']; ?>">
            <div class="mb-4 row">
                <label for="x" class="col-sm-1 col-form-label">X :</label>
                <div class="col-sm-2">
                    <input type="text" class="form-control" required name="x[]">
                </div>
                <label for="y" class="col-sm-1 col-form-label">Y :</label>
                <div class="col-sm-2">
                    <input type="text" class="form-control" required name="y[]">
                </div>
                <label for="status" class="col-sm-1 col-form-label">Status :</label>
                <div class="col-sm-2">
                    <input type="text" class="form-control" required name="status[]">
                </div>
            </div>
        <?php
        } ?>
        <button type="submit" name="simpan" class="btn btn-danger col">Simpan</button>
</form>
<?php
    }
    if (isset($_POST['simpan'])) {
        $xz = 0;
        for ($i = 1; $i <= $_POST['k']; $i++) {
            $x = $_POST['x'];
            $y = $_POST['y'];
            $status = $_POST['status'];
            $con->query("INSERT INTO data VALUES ('','$x[$xz]','$y[$xz]','$status[$xz]')");
            $xz++;
        }
        header('location:index.php');
    }

    include 'footer.php';
?>