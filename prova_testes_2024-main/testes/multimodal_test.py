import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats():
    return StatsN2()

class TestMultimodal:
    @pytest.mark.multimodal
    def test_multimodal_lista_vazia(self, stats):
        assert stats.multimodal([]) == "Não é multimodal"

    @pytest.mark.multimodal
    def test_multimodal_moda_unico_valor(self, stats):
        assert stats.multimodal([1, 1, 1, 1, 1]) == "Não é multimodal"

    @pytest.mark.multimodal
    def test_multimodal_multiplas_modas(self, stats):
        assert stats.multimodal([1, 2, 2, 3, 3, 4, 5, 5]) == [2, 3, 5]

    @pytest.mark.xfail
    @pytest.mark.multimodal
    def test_multimodal_erro_proposital(self, stats):
        assert stats.multimodal([1, 2, 3, 4, 5]) == [1]
