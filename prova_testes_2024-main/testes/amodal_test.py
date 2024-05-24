import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats():
    return StatsN2()

class TestAmodal:
    @pytest.mark.amodal
    def test_amodal_lista_vazia(self, stats):
        assert stats.amodal([]) == "Não existe moda"

    @pytest.mark.amodal
    def test_amodal_sem_moda(self, stats):
        assert stats.amodal([1, 2, 3, 4, 5]) == "Não existe moda"

    @pytest.mark.amodal
    def test_amodal_com_moda(self, stats):
        assert stats.amodal([1, 2, 2, 3, 3, 3, 4, 4, 5]) == "Existe moda"

    @pytest.mark.xfail
    @pytest.mark.amodal
    def test_amodal_erro_proposital(self, stats):
        assert stats.amodal([1, 2, 3, 4, 5]) == "Existe moda"
