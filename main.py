from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__) # En app se encuentra nuestro servidor web de Flask

# La barra (el slash) se conoce como la página de inicio (página home).
# Vamos a definir para esta ruta, el comportamiento a seguir.
@app.route("/")   # @"nombre del servidor web".route("ruta")
def home():
    todas_las_tareas = db.session.query(Tarea).all() #consultamos y almacenamos todas las tareas de la base de datos.
    #Ahora en la variable todas_las_tareas se tienen almacenadas todas las tareas. Vamos a entregar esta variable al
    #template index.html
    for i in todas_las_tareas:
        print(i)
    return render_template("index.html", lista_de_tareas=todas_las_tareas)   # vinculación de index.html y main.py
                 # se renderiza/carga el html y enviamos a index.html la lista de tareas mediante la variable lista_de_tareas

@app.route("/crear-tarea", methods=["POST"])
def crear():
    tarea = Tarea(contenido=request.form["contenido_tarea"], categoria=request.form["categoria_seleccionada"], hecha=False)
                            # con request.form accedemos a los inputs de index.html
    db.session.add(tarea)   #Añadir el objeto de Tarea a la base de datos
    db.session.commit()     #Ejecutar la operación pendiente de la base de datos
    return redirect(url_for("home"))  #volver a la función home() y por tanto, a la página principal

@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).delete() # Se busca dentro de la base de datos aquel registro cuyo id
    # coincida con el aportado por el parámetro de la ruta. Cuando se encuentra se elimina
    db.session.commit()  # Ejecutar la operacion pendiente de la base de datos
    return redirect(url_for("home")) # Esto nos redirecciona a la funcion home() y si todo ha ido bien, al refrescar, la tarea
    #eliminada ya no aparecera en el listado

@app.route("/editar-tarea/<id>")
def editar(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).first()  # almacenamos la tarea a editar en la variable tarea
    print(tarea.contenido)
    return render_template("editar.html", tarea_antigua=tarea)   # vinculación de editar.html y main.py
                 # se renderiza/carga el html y enviamos a editar.html la tarea a editar mediante la variable tarea_antigua

@app.route("/actualizar-tarea/<id>", methods=["POST"])
def actualizar(id):
    db.session.query(Tarea).filter_by(id_tarea=id).delete()
    tarea = Tarea(contenido=request.form["tarea_actualizada"], categoria=request.form["categoria_actualizada"], hecha=False)
                            # con request.form accedemos a los inputs de index.html
    db.session.add(tarea)   #Añadir el objeto de Tarea a la base de datos
    db.session.commit()     #Ejecutar la operación pendiente de la base de datos
    return redirect(url_for("home"))  #volver a la función home() y por tanto, a la página principal


@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)  #creamos la base de datos
    app.run(debug=True) # arrancamos el servidor. El debug=True hace que cada vez que reiniciemos el
                        # servidor o modifiquemos codigo, el servidor de Flask se reinicie solo
