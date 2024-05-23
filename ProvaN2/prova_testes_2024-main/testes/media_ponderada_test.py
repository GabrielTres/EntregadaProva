import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats():
    return StatsN2()

@pytest.fixture
def lista_numeros_exemplo():
    return [1, 2, 3]

@pytest.fixture
def lista_exemplo():
    return [0.2, 0.3, 0.5]

def test_media_ponderada_lista_vazia(stats):
    assert stats.media_ponderada([], []) == 0

def test_media_ponderada_lista(stats, lista_numeros_exemplo, lista_exemplo):
    assert stats.media_ponderada(lista_numeros_exemplo, lista_exemplo) == 2.3

def test_media_ponderada_lista_pesos_zeros(stats, lista_numeros_exemplo):
    with pytest.raises(ValueError):
        stats.media_ponderada(lista_numeros_exemplo, [0, 0, 0])

@pytest.mark.xfail
def test_media_ponderada_erro_proposital(stats, lista_numeros_exemplo, lista_exemplo):
    assert stats.media_ponderada(lista_numeros_exemplo, lista_exemplo) == 10
