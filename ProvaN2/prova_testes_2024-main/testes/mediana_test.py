import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats():
    return StatsN2()

@pytest.fixture
def lista_exemplo():
    return [1, 2, 3, 4, 5]

class TestMediana:
    @pytest.mark.mediana
    def test_mediana_lista_vazia(self, stats):
        assert stats.mediana([]) == 0

    @pytest.mark.mediana
    def test_mediana_lista_impares(self, stats, lista_exemplo):
        assert stats.mediana(lista_exemplo) == 3

    @pytest.mark.mediana
    def test_mediana_lista_pares(self, stats):
        assert stats.mediana([1, 2, 3, 4]) == 2.5

    @pytest.mark.xfail
    @pytest.mark.mediana
    def test_mediana_erro_proposital(self, stats, lista_exemplo):
        assert stats.mediana(lista_exemplo) == 10
