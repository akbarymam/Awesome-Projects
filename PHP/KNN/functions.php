<?php
if (isset($_POST['submit'])) {
  $dump = explode(';', $_POST['dtraining']);
  $n = count($dump);
  for ($i = 0; $i < $n; $i++) {
    // menghasilkan arr 2D
    $dtraining[$i] = explode(',', $dump[$i]);
  }
  $x = count($dtraining[0]) - 1; // menentukan atribut (-label)
  $kdm = @$_POST['kdm'];
  if ($kdm == 1) {
    $kdm = 0;
  }
  if ($kdm >= $n) {
    $kdm = $n;
  }

  $dtesting = explode(',', $_POST['dtesting']);

  // echo SQRT(pow((7 - 3), 2)  + pow((6 - 5), 2));
  // =SQRT((2-3)^2+(2-5)^2)
}

function urutkan($angka, $n)
{
  $i = 0;
  while ($i < $n) {
    $g[$i] = null;
    $i++;
  }
  $i = 0;
  while ($i < $n) {
    if (!is_null($angka[$i])) {
      $g[$angka[$i]] = $angka[$i];
    }
    $i++;
  }
  return $g;
}

function getDistance($v, $dtesting)
{
  return SQRT(pow(($v[0] - $dtesting[0]), 2)  + pow(($v[1] - $dtesting[1]), 2));
}
function hLabel($dtraining, $n, $test2)
{
  $hgood = 0;
  $hbad = 0;
  $hasil = "";
  for ($i = 0; $i < $n; $i++) {
    if (!is_null($test2[$i])) {
      if ($dtraining[$test2[$i]][2] == "Good") {
        $hgood++;
      }
      if ($dtraining[$test2[$i]][2] == "Bad") {
        $hbad++;
      }
    }

    if (is_null($test2[$i]) || $i == ($n - 1)) {
      if ($hgood > $hbad) {
        $hasil = "Good";
        return $hasil;
      } elseif ($hgood < $hbad) {
        $hasil = "Bad";
        return $hasil;
      } elseif ($hgood == $hbad) {
        $hasil = "Hasil ambigu, harap coba nilai K lain";
        return $hasil;
      }
    }
  }
  return $hasil;
}
