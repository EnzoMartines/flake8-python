from typing import List, Dict, Union


class EstatisticaResumida:

    def __init__(self, agencia, dia) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> dict:
        estatistica: Dict[str, Union[int, str, List[int]]] = {}

        estatistica[f'{self.agencia}-{self.dia}'] = len(clientes_atendidos)

        return estatistica
