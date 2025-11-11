from funciones.multiplicar_monteros import multiplicar_monteros

def test_multiplicar_monteros():
    # Prueba 1: 3 * 4 debe ser 12
    assert multiplicar_monteros(3, 4) == 12
    # Prueba 2: -2 * 5 debe ser -10
    assert multiplicar_monteros(-2, 5) == -10