import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats():
    return StatsN2()

@pytest.fixture
def lista_exemplo():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def lista_pesos_exemplo():
    return [0.2, 0.3, 0.5]
