from sqlite3 import Date
from registro_ig import app
from flask import render_template, request, redirect, url_for, flash
from datetime import date
from registro_ig.forms import MovementForm
from registro_ig.models import delete_by, insert, select_all, select_by

@app.route("/")
def index():
    # consultar todos los movimientos de la base de datos
    registros = select_all
    return render_template("index.html", pageTitle="Todos", data=registros)

def validaFormulario(camposFormulario):
    errores = []
    hoy = date.today().isoformat()
    if camposFormulario['date'] > hoy:
        errores.append("La fecha introducida es el futuro.")

    if camposFormulario['concept'] == "":
        errores.append("Introduce un concepto para la transacción.")

    #La primera condición es para que el número sea distinto de cero
    #la segunda condición es para que el campo no esté vacío
    if camposFormulario["quantity"] == "" or float(camposFormulario["quantity"]) == 0.0:
        errores.append("Introduce una cantidad positiva o negativa.")

    return errores

@app.route("/Alta", methods=["GET", "POST"])
def Alta():
    form = MovementForm()
    if request.method == "GET":
        return render_template("Alta.html", Form=form, PageTitle="Alta")
    else:
        errores = validaFormulario(request.form)
        if not errores:
            insert([form.date.data.isoformat(),
                    form.concept.data,
                    form.quantity.data
                    ])
            return redirect(url_for("index"))        
        else:
            return render_template("new.html" , Form=form)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def borrar(id):
    if request.method == "GET":
        registro = select_by(id)
        if registro:
            return render_template("delete.html", movement=select_by(id))
        else:
            flash("No se encuentra el registro {id}. ")
            return redirect(url_for("index"))                
    else:
        delete_by(id)
        flash("Registro borrado correctamente")
        return redirect(url_for("index"))