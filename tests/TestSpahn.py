from funciones.SumaSpahn import sumarspahn

def test_sumarspahn():
    assert sumarspahn(3, 5) == 8
    assert sumarspahn(-2, 2) == 0