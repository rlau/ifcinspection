<?php

$arguments = $argv;
$to = $arguments[0];
$message = $arguments[1];
$subject = $arguments[2];

mail($to, $subject, $message);

?>

