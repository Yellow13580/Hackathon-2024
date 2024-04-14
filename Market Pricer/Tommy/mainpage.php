<?php
    // File: mainpage.php
   session_start();
?>

<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">

<!--
    by: Jonathan Thang and Sam Hodgdon and Tommy Le
    last modified: 4/13/2024

    you can run this using the URL:
    https://nrs-projects.humboldt.edu/~jt346/hackathon2024/mainpage.php
-->

<head>
    <title> App Name </title>
    <meta charset="utf-8" />

    <link href="mainstyle.css"
          type="text/css" rel="stylesheet" />

          <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
     <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
</head>

<body>
    <?php
        $_SESSION["state"] = "startform";

        if ($_SERVER["REQUEST_METHOD"] == "GET")
        {
    ?>
    <div class="firstpage">
        <h1> Welcome To <br /> Market Pricer </h1>
        <p> 
            Market Pricer is our free-to-use website that will help you shop quickly and efficiently when you need to split
            the cost of one big shopping trip. If you live with other people and shop together, you can split the cost of 
            certain items allowing for easy budgeting between roommates. All you have to do is list how many people
            you want to split it with and your names! 
        </p> 

        <form class="mainform" method="post" action="<?= htmlentities($_SERVER["PHP_SELF"], ENT_QUOTES) ?>">
            <fieldset class="numSplit">
                <label for="numSplit">Number of people splitting the bill:</label>
                <input type="number" id="numSplit" name="numSplit" min="1" max="5" required>
            </fieldset> <br/>
        
            <input type="submit" value="Submit" />     
        </form>
    </div>

    <?php
    }
    else
    {       
        if ($_POST["numSplit"] == 1){
            header("Location: search.php");
        }
        else
        {
            ?>
                <div class="secondpage">
                    <h1 class="billsplit"> Enter who is splitting the bill: </h1>
                    <div class="formy">
                        <form method="post" action="search.php">
                            <fieldset>
                                <?php
                                    $count = 0;
                                    while ($count < $_POST["numSplit"])
                                    {
                                        ?>
                                            <label for="<?= "name" . $count ?>"> Enter name #<?= $count + 1?>: </label>
                                            <input type="text" id="<?= "name" . $count ?>" name="<?= "name" . $count ?>" required /><br />
                                        <?php
                                        $count++;
                                    }
                                    $_SESSION["count"] = $_POST["numSplit"];
                                ?>
                
                                    <input class="sub" type="submit" value="Submit" />
                            </fieldset>
                        </form>
                    </div>
                </div>
            <?php
        }
        ?>
        <?php
    }
    ?>
    </form>
</body>
</html>

