
def busca_arreglo(busca):#el peor ejemplo
    print(f"Buscando en el arreglo : {busca}")
    arreglo_palabras = ["rojo","verde","azul","negro","morado"]

    for item in arreglo_palabras:
        print (f"Palabras : {item}")
    if busca == item:
        print("Palabra encontrada")
        return "Encontrada en arreglo"
    return "No se encontro en el arreglo"
    #if busca in arreglo_palabras:
    #    print("tambien lo encontre")

def busca_in_file(busca):
    file =open ('palabra.txt','r')
    if busca in file.read():
        print("lo encontre con file read")
        return 1
    file = open('groserias.txt','r')
    if busca in file.read():
        print("\n\t\tlo encontre con file read")
        return 3
    file.close()
    return False


def busca_whit_file(busca):
    with open('palabras.txt') as file:
        data = True
        while data:
            data= file.readline()
            print(data)

#texto = "Mi casa es green"

#texto_analizar = texto.split()
#print(texto_analizar)
#for item in texto_analizar:
#    print(f"analizando{item}")
#    analisis = busca_arreglo(item)
#    if not analisis:
#        print("El texto contiene algo invalido")
#    print(busca_in_file(item))