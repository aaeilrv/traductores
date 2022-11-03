# Traductores e Interpretadores
# Valeria Vera 16-11233
# Giacomo Tosone 14-11085

import sys
import func_lexer as lexer

# Funcion main, ejemplo de entrada: python lexer.py archivo.gcl
# Solo se aceptan archivos .gcl
# Se debe colocar en el archivo.gcl el codigo a ser analizado

def main():
    correct = []
    incorrect = []
    try:
        filename = sys.argv[1]
    except:
        print("Introduzca nombre de archivo (python main.py input.gcl)")
        return 0
    doc = sys.argv[1].split(".")
    if doc[-1] == "gcl":
        file = open(filename,"r")
        row = 1
        try:
            for line in file.readlines():
                incorrect = lexer.work(line,row, correct)            
                row += 1
        except:
           print("archivo no existe")
           return 1
    else:
        print("archivo solo puede ser de tipo .gcl")
    
    # Se imprime en consola y crea un archivo de salida.
    with open('lexer_result.out', 'w') as f:
        if incorrect == []:
            for i in correct:
                f.write(i)
                print(i)
                if i != correct[-1]:
                    f.write("\n")
        else:
            for i in incorrect:
                f.write(i)
                print(i)
                if i != correct[-1]:
                    f.write("\n")

if __name__ == "__main__":
    main()