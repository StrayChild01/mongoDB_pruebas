# Cómo usar múltiples bases de datos en django

- Primero, se tiene que instalar el plugin de django para la BD, en este caso, Cassandra:

```Shell
pip install django-cassandra-engine
```

- Después se tiene que modificar lo siguiente en settings.py:

```Python

#Se agrega aquí, para que se pueda usar el plugin
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Se agrega el plugin de cassandra
    'django_cassandra_engine',
]

#Se definen los parámetros de la BD para la conexión
DATABASES = {
    # Esta es la BD de default
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # Se agrega la BD de cassandra
    'cassandra_db': {
    'ENGINE': 'django_cassandra_engine',
    'NAME': 'ks_test',
    'TEST_NAME': 'test',
    'HOST': '192.168.1.30',
    'OPTIONS': {
        'replication': {
            'strategy_class': 'SimpleStrategy',
            'replication_factor': 1
        }
    }
  }
}
```

- Para usarlo dentro de models.py se agrega lo siguiente:

```Python
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
```

- Después, para sincronizar el modelo, se ejecuta lo siguiente:

```Python
python manage.py sync_cassandra
```
