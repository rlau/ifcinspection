<?php
$arguments = $argv;
$to = $arguments[1];
$message = $arguments[2];
$subject = $arguments[3];
$from = $arguments[4];

$header = 'From: {$from}' . "\r\n" .
	'Reply-To: {$from}' . "\r\n";
mail($to, $subject, $message, $header);

?>

