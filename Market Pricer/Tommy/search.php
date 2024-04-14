<?php
    // File: search.php
    session_start();
    if(!empty($_GET)){
        $_SESSION = array_merge($_SESSION, $_GET);
    }
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);
    require_once("hum_conn_no_login.php");

    if(!isset($_SESSION['cart']) || !is_array($_SESSION['cart'])){
        $_SESSION['cart'] = array();
    }

    if(isset($_SESSION["count"])){
        $count5 = 0;
        while($count5 < $_SESSION["count"])
        {
            if(isset($_POST["name".$count5])){
                $name = strip_tags($_POST["name" . $count5]);
                $_SESSION["name".$count5] = $name;
            }
            $count5++;
        }
    }
?>

<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">

<head>
    <title> Search Items </title>
    <meta charset="utf-8" />
    <link href="https://nrs-projects.humboldt.edu/~st10/styles/normalize.css" type="text/css" rel="stylesheet" />
</head>

<body>
    <h2>Enter shopping list items here:</h2>
    <form method="post">
        <input type="text" name="search" placeholder="Search for items..." />
        <input type="submit" name="search_btn" value="Search" />
    </form>

    <?php
    $conn = hum_conn_no_login();
    if($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['search_btn'])){
        $search = strip_tags(strtolower('%' . $_POST['search'] . '%'));
        $query = "select * from item where lower(item_name) like :search";
        $stmt = oci_parse($conn, $query);
        oci_bind_by_name($stmt, ':search', $search);
        oci_execute($stmt);
        $result = false;

        echo "<form method='post' id='something'>";
        while($row = oci_fetch_assoc($stmt)){
            $result = true;
            $item_name = $row["ITEM_NAME"];
            $item_price = $row["ITEM_PRICE"];
            $item_price_per_unit = $row["ITEM_PRICE_PER_UNIT"];
            
            echo "<input type='checkbox' name='items[]' value='" . $item_name . "'>" . $item_name . " - $" . $item_price . " (" . $item_price_per_unit . " per unit) - " . "<br/>";
            echo "Quantity: <input type='number' name='quantity[" . $item_name . "]' min='1' value='1'><br/>";
        }
        if($result){
            echo "<input type='submit' name='add_to_cart' value='Add to Cart' />";
        } else{
            echo "<p>No results found</p>";
        }
        echo "</form>";
    }

    // Check if the add to cart button is clicked
    if($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['add_to_cart'])){
        // Get the selected items and their quantities
        $items = isset($_POST['items']) ? $_POST['items'] : array();
        $quantities = isset($_POST['quantity']) ? $_POST['quantity'] : array();

        // Create a new array to store the updated cart
        $updatedCart = $_SESSION['cart'];

        // Add or update the items in the cart
        foreach($items as $item){
            $quantity = isset($quantities[$item]) ? intval($quantities[$item]) : 1;
            $query = "select item_price, item_price_per_unit from item where item_name = :item";
            $stmt = oci_parse($conn, $query);
            oci_bind_by_name($stmt, ':item', $item);
            oci_execute($stmt);
            $row = oci_fetch_assoc($stmt);
            $price = $row['ITEM_PRICE'];
            $price_per_unit = $row['ITEM_PRICE_PER_UNIT'];

            if(isset($updatedCart[$item])){
                $updatedCart[$item]['quantity'] += $quantity;
            } else{
                $updatedCart[$item] = array(
                    'quantity' => $quantity,
                    'price' => $price,
                    'price_per_unit' => $price_per_unit
                );
            }
        }

        // Update the session cart with the new cart data
        $_SESSION['cart'] = $updatedCart;
    }
    // Check if the remove from cart button is clicked
    if($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['remove_from_cart'])){
        $item_to_remove = $_POST['remove_from_cart'];
        if(isset($_SESSION['cart'][$item_to_remove])){
            unset($_SESSION['cart'][$item_to_remove]);
        }
    }
    ?>

    <h2>Shopping Cart</h2>
    <div id="cart">
        <?php
        if(!empty($_SESSION['cart'])){
            echo "<table>";
            echo "<tr><th>Item</th><th>Quantity</th><th>Price</th><th>Total</th><th>Action</th></tr>";
            foreach($_SESSION['cart'] as $item => $details){
                if(is_array($details)){
                    $total = $details['quantity'] * $details['price'];
                    echo "<tr>";
                    echo "<td>" . $item . "</td>";
                    echo "<td>" . $details['quantity'] . "</td>";
                    echo "<td>$" . $details['price'] . "</td>";
                    echo "<td>$" . number_format($total, 2) . "</td>";
                    echo "<td>
                        <form method='post'>
                            <input type='hidden' name='remove_from_cart' value='" . $item . "' />
                            <input type='submit' value='Remove' />
                        </form>
                        </td>";
                    echo "</tr>";
                }
            }
            echo "</table>";
            echo "<form method='post' action='checkout.php'>";
            echo "<input type='submit' value='Checkout'/>";
            echo "</form>";
        } else{
            echo "Your cart is empty.";
        }
        oci_close($conn);
        ?>
    </div>
</body>
</html>
