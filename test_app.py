from app import app, sumar


def test_sumar():
    assert sumar(2, 3) == 5


def test_sumar_negativos():
    assert sumar(-2, -3) == -5


def test_pagina_inicio():
    cliente = app.test_client()

    respuesta = cliente.get("/")

    assert respuesta.status_code == 200


def test_endpoint_suma():
    cliente = app.test_client()

    respuesta = cliente.get("/suma?a=10&b=5")

    assert respuesta.status_code == 200

    datos = respuesta.get_json()

    assert datos["resultado"] == 15