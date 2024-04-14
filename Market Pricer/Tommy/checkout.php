<?php
    // File: Checkout.php
    session_start();
    require_once("hum_conn_no_login.php");

    // Retrieve the cart data and people names from the session
    $cart = isset($_SESSION['cart']) ? $_SESSION['cart'] : array();
    $people = array();
    if(isset($_SESSION["count"])){
        for($i = 0; $i < $_SESSION["count"]; $i++){
            if(isset($_SESSION["name" . $i])){
                $people[$_SESSION["name" . $i]] = array(); // Initialize an empty array for each person
            }
        }
    }
?>
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">

<head>
    <title>Checkout</title>
    <meta charset="utf-8"/>
    <link href="https://nrs-projects.humboldt.edu/~st10/styles/normalize.css" type="text/css" rel="stylesheet"/>
    <link href="final.css" type="text/css" rel="stylesheet"/>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">

</head>

<body>
    <h2 id="check">Checkout</h2>
    <?php if(!empty($cart)){ ?>
        <form method="post">
            <table>
                <tr>
                    <th>Item Name</th>
                    <th>Price</th>
                    <th>Price Per Unit</th>
                    <?php foreach($people as $person_name => $value){ ?>
                        <th><?= $person_name ?></th>
                    <?php } ?>
                </tr>
                <?php
                    $total_cost = 0;
                    foreach($cart as $item => $details){
                    $price = $details['price'];
                    $quantity = $details['quantity'];
                    $price_per_unit = $details['price_per_unit'];
                    $item_total = $price * $quantity;
                    $total_cost += $item_total;
                ?>
                <tr>
                    <td><?= $item ?></td>
                    <td>$<?= number_format($item_total, 2) ?></td>
                    <td><?= $price_per_unit ?></td>
                    <?php foreach($people as $person_name => $value){ ?>
                        <td><input type="checkbox" name="split[<?= $person_name ?>][<?= $item ?>]" value="<?= $item_total ?>"/></td>
                    <?php } ?>
                </tr>
                <?php } ?>
            </table>
            <p>Total Cost: $<?= number_format($total_cost, 2) ?></p>
            <input type="submit" name="calculate" value="Calculate Split"/>
        </form>
    <?php } else{ ?>
                <p>Your cart is empty.</p>
    <?php } ?>

    <?php
        if($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['calculate'])){
            $person_totals = array_fill_keys(array_keys($people), 0);
            foreach($_POST['split'] as $person_name => $items){
                foreach($items as $item_name => $item_total){
                    $num_ppl = 0;
                    foreach($_POST['split'] as $p_name => $i){
                        if(isset($i[$item_name])){
                            $num_ppl++;
                        }
                    }
                    if($num_ppl > 0){
                        $person_totals[$person_name] += $item_total / $num_ppl;
                    }
                }
            }
            echo "<h3>Split Totals: </h3>";
            echo "<ul>";
            foreach($person_totals as $person_name => $total){
                echo "<li>$person_name: $" . number_format($total, 2) . "</li>";
            }
            echo "</ul>";
            echo "<a href='mainpage.php'> Return to Home Page </a>";
        }
        session_destroy();
        oci_close($conn);
    ?>
</body>
</html>
