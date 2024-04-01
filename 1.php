<?php

$target = 900900;
$products = [];

for ($i = 1; $i <= sqrt($target); $i++) {
    if ($target % $i == 0) {
        $factor1 = $i;
        $factor2 = $target / $i;

        if ($factor1 < $factor2) {
            $products[] = "$factor1 * $factor2 = $target";
        }
    }
}

foreach ($products as $product) {
    echo $product . "\n";
}

?>