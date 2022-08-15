from typing import Union

from fila_normal import filanormal
from fila_prioritaria import FilaPrioritaria
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIMORITARIA


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila) -> Union[filanormal, FilaPrioritaria]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return filanormal()
        elif tipo_fila == TIPO_FILA_PRIMORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError("Tipo de fila não existe")
