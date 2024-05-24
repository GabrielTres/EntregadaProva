import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats():
    return StatsN2()

class TestVariancia:
    @pytest.mark.variancia
    def test_variancia_lista_vazia(self, stats):
        assert stats.variancia([]) == 0

    @pytest.mark.variancia
    def test_variancia_lista_nao_vazia(self, stats):
        assert stats.variancia([1, 2, 3, 4, 5]) == pytest.approx(2.5)

    @pytest.mark.xfail
    @pytest.mark.variancia
    def test_variancia_erro_proposital(self, stats):
        assert stats.variancia([1, 2, 3, 4, 5]) == 10
