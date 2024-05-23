import pytest
from stat_funcs import StatsN2

class TestMedia:
    @pytest.fixture
    def stats(self):
        return StatsN2()

    @pytest.mark.media
    def test_media_lista_vazia(self, stats):
        assert stats.media([]) == 0

    @pytest.mark.media
    def test_media_lista(self, stats):
        assert stats.media([1, 2, 3, 4, 5]) == 3

    @pytest.mark.media
    @pytest.mark.parametrize("lista, resultado", [([1, 2, 3, 4], 2.5), ([5, 5, 5, 5], 5)])
    def test_media_parametrizada(self, stats, lista, resultado):
        assert stats.media(lista) == resultado

    @pytest.mark.xfail
    @pytest.mark.media
    def test_media_erro_proposital(self, stats):
        assert stats.media([1, 2, 3, 4, 5]) == 10
