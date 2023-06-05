import os

def imprimir_estructura_directorio(directorio, nivel=0):
    for item in os.listdir(directorio):
        ruta = os.path.join(directorio, item)
        if os.path.isdir(ruta):
            print("  " * nivel + "|-- " + item + "/")
            imprimir_estructura_directorio(ruta, nivel + 1)
        else:
            print("  " * nivel + "|-- " + item)

# Ejemplo de uso:

directorio_raiz = "RDATA/CrisisMMD_v2.0/json"
imprimir_estructura_directorio(directorio_raiz)
print("")
directorio_raiz2 = "RDATA/CrisisMMD_v2.0/annotations"
imprimir_estructura_directorio(directorio_raiz2)