import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats():
    return StatsN2()

class TestDpadrao:
    @pytest.mark.dpadrao
    def test_dpadrao_variancia_zero(self, stats):
        assert stats.dpadrao(0) == 0

    @pytest.mark.dpadrao
    def test_dpadrao_variancia_positiva(self, stats):
        assert stats.dpadrao(4) == pytest.approx(2)

    @pytest.mark.xfail
    @pytest.mark.dpadrao
    def test_dpadrao_erro_proposital(self, stats):
        assert stats.dpadrao(4) == 3
