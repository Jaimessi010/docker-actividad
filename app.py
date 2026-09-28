from flask import Flask, jsonify, request
import os

app = Flask(__name__)


# -----------------------------
# Funciones de la aplicación
# -----------------------------
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")

    return a / b

# -----------------------------
# Rutas
# -----------------------------

@app.route("/")
def inicio():
    return jsonify({
        "proyecto": "Actividad Docker",
        "descripcion": "API desarrollada con Python y Flask",
        "estado": "Aplicación ejecutándose correctamente",
        "version": "1.0.0"
    })


@app.route("/salud")
def salud():
    return jsonify({
        "status": "OK",
        "mensaje": "El servicio está funcionando correctamente"
    })


@app.route("/suma")
def suma():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))

        resultado = sumar(a, b)

        return jsonify({
            "operacion": "suma",
            "a": a,
            "b": b,
            "resultado": resultado
        })

    except (TypeError, ValueError):
        return jsonify({
            "error": "Debes enviar valores numéricos para a y b"
        }), 400


@app.route("/resta")
def resta():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))

        resultado = restar(a, b)

        return jsonify({
            "operacion": "resta",
            "a": a,
            "b": b,
            "resultado": resultado
        })

    except (TypeError, ValueError):
        return jsonify({
            "error": "Debes enviar valores numéricos para a y b"
        }), 400


@app.route("/multiplicacion")
def multiplicacion():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))

        resultado = multiplicar(a, b)

        return jsonify({
            "operacion": "multiplicacion",
            "a": a,
            "b": b,
            "resultado": resultado
        })

    except (TypeError, ValueError):
        return jsonify({
            "error": "Debes enviar valores numéricos para a y b"
        }), 400


@app.route("/division")
def division():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))

        resultado = dividir(a, b)

        return jsonify({
            "operacion": "division",
            "a": a,
            "b": b,
            "resultado": resultado
        })

    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 400

    except TypeError:
        return jsonify({
            "error": "Debes enviar valores numéricos para a y b"
        }), 400


# -----------------------------
# Manejador de errores
# -----------------------------

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return jsonify({
        "error": "Ruta no encontrada",
        "codigo": 404
    }), 404


# -----------------------------
# Ejecutar aplicación
# -----------------------------

if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 5001))

    app.run(
        host="0.0.0.0",
        port=puerto,
        debug=False
    )