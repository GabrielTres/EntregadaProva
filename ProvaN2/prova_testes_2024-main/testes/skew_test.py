import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats():
    return StatsN2()

class TestSkew:
    @pytest.mark.skew
    def test_skew_distribuicao_normal(self, stats):
        assert stats.skew([1, 2, 3, 4, 5]) == "Distribuição normal"

    @pytest.mark.skew
    def test_skew_distribuicao_positiva(self, stats):
        assert stats.skew([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "Distribuição positiva"

    @pytest.mark.skew
    def test_skew_distribuicao_negativa(self, stats):
        assert stats.skew([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == "Distribuição negativa"

    @pytest.mark.xfail
    @pytest.mark.skew
    def test_skew_erro_proposital(self, stats):
        assert stats.skew([1, 2, 3, 4, 5]) == "Distribuição positiva"
