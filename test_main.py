from main import calcular_promedio

def test_calcular_promedio_valores():
    assert calcular_promedio([2, 4, 6]) == 4.0

def test_calcular_promedio_vacio():
    assert calcular_promedio([]) == 0