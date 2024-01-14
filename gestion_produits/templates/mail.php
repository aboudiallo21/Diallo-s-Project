<!-- mail.php -->
<?php
if($_POST) {
    $name = $_POST['name'];
    $surname = $_POST['surname'];
    $email = $_POST['email'];
    $message = $_POST['message'];

    // Destination email address
    $destEmail = "22314@esp.mr";

    // Prepare email body
    $body = "Nom: {$name}\n";
    $body .= "Prénom: {$surname}\n";
    $body .= "Email: {$email}\n";
    $body .= "Message: {$message}\n";

    // Send email
    $success = mail($destEmail, "Nouveau message du formulaire de contact", $body, "From: {$email}");

    if ($success) {
        echo "Votre message a bien été envoyé.";
    } else {
        echo "Il y a eu une erreur lors de l'envoi de votre message.";
    }
}
?>
