#! /usr/bin/python3

import pymongo
import json

mi_contenido_archivo = ""
with open(file="/home/straychild01/Documents/miArchivo.txt", \
        mode="r+") as mi_archivo:
    for linea_actual in mi_archivo.readlines():
        mi_contenido_archivo += linea_actual

mi_contenido_archivo = mi_contenido_archivo.replace('"','\\"')
mi_contenido_archivo = mi_contenido_archivo.replace('\n','\\n')

mi_contenido_json = '{{' \
                    '"_id": "{0}",' \
                    ' "name": "{1}",' \
                    ' "age": {2},' \
                    ' "contenido_documento": "{3}"' \
                    '}}'.format("100", "Ana", "50", mi_contenido_archivo)

print(mi_contenido_json)
mi_json = json.loads(mi_contenido_json)
print(mi_json)

cliente = pymongo.MongoClient("mongodb://localhost:27017/")
bd = cliente['mi_script']
print(bd)
mi_colleccion = bd["miprueba"]
mi_colleccion.insert_one(mi_json)
for registro_actual in mi_colleccion.find():
    print(registro_actual)

cliente.close()