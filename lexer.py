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
                #lexer.work(line,row, correct)    
                row += 1
        except:
           print("archivo no existe")
           return 1
    else:
        print("archivo solo puede ser de tipo .gcl")
    
    if incorrect == []:
        for i in correct:
            print(i)
    else:
        for i in incorrect:
            print(i)

if __name__ == "__main__":
    main()