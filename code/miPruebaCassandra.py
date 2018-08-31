from cassandra.cluster import Cluster
import uuid

# Este código tiene las siguientes suposiciones:
# - El keyspace ks_test ha sido creado:
#     create keyspace ks_test
#       with replication = {
#                           'class': 'SimpleStrategy',
#                            'replication_factor' : 1
#                           };
# - La tabla test ha sido creada
#     create table test (id uuid primary key, name text);

# Código inspirado en:
# https://datastax.github.io/python-driver/getting_started.html

# Conectarse al cluster
mi_cluster = Cluster(["192.168.1.30"], port=9042)

# abrir sesión
mi_sesion = mi_cluster.connect()

# seleccionar keyspace
mi_sesion.set_keyspace("ks_test")

# ejecutar query
mi_sql = "select * from ks_test.test"
mi_query = mi_sesion.execute(mi_sql)

# iterar el resultado de mi_query
for registro_actual in mi_query:
    # Registro actual es una namedtuple, por tanto se puede acceder a los
    # valores con los nombres o las posiciones:
    # 1.- registro_actual.id, registro_actual.name
    # 2.- registro_actual[0], registro_actual[1]
    # Para obtener los nombres de los campos, se usa minamedtuple._fields
    print("Registro actual: id = {}, name = {}".format(
        registro_actual.id, registro_actual.name)
    )

mi_sql = "insert into ks_test.test(id, name) values ({}, '{}')"
my_query = mi_sesion.execute(mi_sql.format(uuid.uuid1(), "Mi inserción con python"))

print("--------------------")
mi_sql = "select * from ks_test.test"
mi_query = mi_sesion.execute(mi_sql)
for registro_actual in mi_query:
    print("Contenido tabla: id = {}, name = {}".format(
        registro_actual[0], registro_actual[1])
    )


# print("--------------------")
# mi_sql = "delete from ks_test.test where id = '{}'"
# mi_query = mi_sesion.execute(mi_sql.format("ba3fb48-a7b8-11e8-a704-54e1ad9f18d8"))

print("--------------------")
mi_sql = "select * from ks_test.test"
mi_query = mi_sesion.execute(mi_sql)
for registro_actual in mi_query:
    print("Contenido tabla: id = {}, name = {}".format(
        registro_actual[0], registro_actual[1])
    )

# cerrar la conexión
mi_cluster.shutdown()