import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats():
    return StatsN2()

class TestUnimodal:
    @pytest.mark.unimodal
    def test_unimodal_lista_vazia(self, stats):
        assert stats.unimodal([]) == "Não é unimodal"

    @pytest.mark.unimodal
    def test_unimodal_unica_moda(self, stats):
        assert stats.unimodal([1, 2, 2, 3, 4, 4, 4, 5]) == 4

    @pytest.mark.unimodal
    def test_unimodal_multiplas_modas(self, stats):
        assert stats.unimodal([1, 2, 3, 4, 5]) == "Não é unimodal"

    @pytest.mark.xfail
    @pytest.mark.unimodal
    def test_unimodal_erro_proposital(self, stats):
        assert stats.unimodal([1, 2, 3, 4, 5]) == 10
