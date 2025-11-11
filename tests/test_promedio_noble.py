from funciones.promedio_noble import promedio_noble

def test_promedio_noble():
    assert promedio_noble([2, 4, 6]) == 4
    assert promedio_noble([]) is None
