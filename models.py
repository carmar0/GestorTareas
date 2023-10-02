from sqlalchemy import Column, Integer, String, Boolean
import db     # para poder acceder al fichero db.py

class Tarea(db.Base):
    # primero configuramos lo referente  a la base de datos
    __tablename__ = "tarea"  #Para que cuando el ORM cree la tabla en la base de datos, use este nombre de tabla
    __table_args__ = {'sqlite_autoincrement': True}  # Automaticamente la Primary Key de la tabla se convierte en autocincremental. Se puede
                                                      # desactivar poniendolo a False
    id_tarea = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)  #Contenido de la tarea, un texto de máximo 200 caracteres
    categoria = Column(String(200))
    hecha = Column(Boolean)

    # ahora configuramos el constructor y str de la clase
    def __init__(self, contenido, categoria, hecha):
        self.contenido = contenido
        self.categoria = categoria
        self.hecha = hecha

    def __str__(self):
        return "Tarea: {} -> {} -> {} -> {}".format(self.id_tarea, self.contenido, self.categoria, self.hecha)