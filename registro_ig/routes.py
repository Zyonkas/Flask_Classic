from registro_ig import app
from flask import render_template

@app.route("/")
def index():
    # consultar todos los movimientos de la base de datos
    return render_template("index.html", pageTitle="Todos", 
                        data=[
                            {"id": 1, "date": "2022-01-01", "concept": "Sueldo", "quantity": 1000},
                            {"id": 2, "date": "2022-01-05", "concept": "Reyes", "quantity": -100}
                            ])