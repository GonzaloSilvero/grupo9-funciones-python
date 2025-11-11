from funciones.multipspahn import multipspahn

def test_multipspahn():
    assert multipspahn(3, 5) == 15
    assert multipspahn(-2, 2) == -4