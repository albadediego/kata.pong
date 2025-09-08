'''
from figura_class import Raqueta, Pelota

objRaqueta = Raqueta(0,500)
objPelota = Pelota(0,300)

print(objRaqueta.derecha)
print(objRaqueta.izquierda)
print(objRaqueta.arriba)
print(objRaqueta.abajo)
print("##############################")
print(objPelota.derecha)
print(objPelota.izquierda)
print(objPelota.arriba)
print(objPelota.abajo)
'''

'''
def datosPersonales(*args):
    for datos in args:
        print(datos)

datosPersonales("Jose", "Martinez", 25, True, [1,2,3])

def nombres(apellido):
    return "Jose Alfredo "+ apellido

def apellidos(ape):
    return ape

nombres_apelidos = nombres(apellidos("Perez Ruiz"))
print(nombres_apelidos)
'''

'''
def mover_mano()->str:
    return "izquierda"

if mover_mano() == "izquierda":
    print("zurdo")
else:
    print("diestro")
'''
