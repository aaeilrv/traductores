import sys
import lexer as lexer

# Funcion main, ejemplo de entrada: python main.py archivo.gcl
# Solo se aceptan archivos .gcl
# Se debe colocar en el archivo.gcl el codigo a ser analizado

def main():
    try:
        filename = sys.argv[1]
    except:
        print("Introduzca nombre de archivo (python main.py input.gcl)")
        return 0
    doc = sys.argv[1].split(".")
    if doc[-1] == "gcl":
        try:
            file = open(filename,"r")
            lines = file.read()
            lexer.work(lines)
        except:
            print("archivo no existe")
            return 1
    else:
        print("arhivo solo puede ser de tipo .gcl")
   


if __name__ == "__main__":
    main()