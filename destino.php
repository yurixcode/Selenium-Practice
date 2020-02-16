<html>
    <head>
        <title>Páginas de destino</title>
    </head>

    <body>
        <?php
            $nombre = $_POST['nombre'];
            $email = $_POST['email'];
            $telefono = $_POST['telefono'];

            if(empty($nombre) or empty($email) or empty($telefono)) 
            {echo "Completa todos los campos por favor.";}
            else{echo "Hola " . $nombre . "<br> Su email es: " . $email . ". <br>Su número de tlf es: " . $telefono;}

        ?>


    </body>


</html>