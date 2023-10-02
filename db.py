from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# engine --> permite a sqlalchemy (ORM) comunicarse con la base de datos
engine = create_engine('sqlite:///database/tareas.db', connect_args={'check_same_thread': False})
# Advertencia, crear el engine no conecta inmediatamente a la base de datos, eso lo hacemos más adelante
# Con esta primera linea estamos diciendo que el motor de la base de datos es sqlite, que almacenamos la base de datos
# dentro de la carpeta database y que se llama personas

# Ahora creamos la sesión, lo que nos permite realizar transacciones (operaciones) dentro de nuestra BD
Session = sessionmaker(bind=engine)
session = Session()

# Ahora vamos al fichero models.py y en los modelos (clases) donde queramos que se transformen en tablas,
# le añadiremos como herencia esta variable Base, y esto se encargara de mapear  y vincular la clase a la tabla
Base = declarative_base()
