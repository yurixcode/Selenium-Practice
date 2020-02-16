<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Ejemplo 2</title>

        <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
        <script>
            function sleep(time) {
                return new Promise( (resolve) => setTimeout(resolve, time));
            }

            sleep(5000).then(() => {
                $('form').append("<tr><td> <input type='submit' name='enviar' id='enviar' value='Enviar datos' /> </td></tr>")
            });
        </script>

    </head>
    <body>
        <h1>Curso Python Web scraping</h1>
        <form action="destino.php" method="post">
            Rellene los siguientes campos:<br><br>
            <table>
                <tr>
                    <td>Nombre:</td>
                    <td>
                        <input type="text" name="nombre" id="nombre" size="50" maxLength="100">
                    </td>
                </tr>
                <tr>
                    <td>Email:</td>
                    <td>
                        <input type="text" name="email" id="email" size="50" maxLength="100">
                    </td>
                </tr>
                <tr>
                    <td>Teléfono:</td>
                    <td>
                        <input type="text" name="telefono" id="telefono" size="50" maxLength="100">
                    </td>
                </tr>

            </table>

        </form>

        
    </body>
</html>