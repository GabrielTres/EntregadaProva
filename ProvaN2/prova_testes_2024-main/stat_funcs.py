import statistics
import numpy as np
from collections import Counter
import scipy


class StatsN2:

    @staticmethod
    def media(lista) -> float:
        if not lista:
            return 0
        return sum(lista) / len(lista)

    @staticmethod
    def media_ponderada(lista, pesos) -> float:
        return np.average(lista, weights=pesos)

    @staticmethod
    def mediana(lista) -> float:
        n = len(lista)
        if n == 0:
            return 0
        if n % 2:
            median_ = sorted(lista)[round(0.5*(n - 1))]
        else:
            x_ord, index = sorted(lista), round(0.5 * n)
            median_ = 0.5 * (x_ord[index - 1] + x_ord[index])
        return median_

    @staticmethod
    def unimodal(lista):
        counts = Counter(lista)
        max_count = max(counts.values())
        modas = [num for num, count in counts.items() if count == max_count]
        if len(modas) == 1:
            return modas[0]
        else:
            return "Não é unimodal"

    @staticmethod
    def multimodal(lista):
        counts = Counter(lista)
        max_count = max(counts.values())
        modas = [num for num, count in counts.items() if count == max_count]
        if len(modas) > 1:
            return modas
        else:
            return "Não é multimodal"

    @staticmethod
    def amodal(lista):
        counts = Counter(lista)
        if all(count == 1 for count in counts.values()):
            return "Não existe moda"
        else:
            return "Existe moda"

    @staticmethod
    def variancia(lista) -> float:
        n = len(lista)
        media_ = sum(lista) / n
        var_ = sum((item - media_)**2 for item in lista) / (n - 1)
        return var_

    @staticmethod
    def dpadrao(var) -> float:
        return var ** 0.5

    @staticmethod
    def skew(lista) -> str:
        y = np.array(lista)
        skewness = scipy.stats.skew(y, bias=False)
        if skewness == 0:
            return "Distribuição normal"
        elif skewness < 0:
            return "Distribuição negativa"
        else:
            return "Distribuição positiva"
