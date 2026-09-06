from typing import Optional
from ..problema_baldes import ProblemaBaldes
from colorama import Fore

class EstadoBacktracking:

    REGRAS = [
        "enche_b3",
        "enche_b5",
        "esvazia_b3",
        "esvazia_b5",
        "b3_to_b5",
        "b5_to_b3",
    ]
    
    def __init__(self, pai: Optional["EstadoBacktracking"] = None, baldes: ProblemaBaldes = None, regra_geradora: Optional[str] = None, ordem_reversa: bool = False, logs: bool = False):
        self.baldes = baldes if baldes else ProblemaBaldes()
        self.pai = pai
        self.regra_geradora = regra_geradora
        self.proxima_regra = 0
        self.impasse = False
        self.ordem_reversa = ordem_reversa
        self.logs = logs

    def _calcular_possiveis(self):
        possiveis = []
        for nome_regra in self.REGRAS:
            candidato_baldes = self.baldes.clonar()
            try:
                getattr(candidato_baldes, nome_regra)()
                possiveis.append(nome_regra)
            except Exception:
                continue
        return possiveis
      
    def gerar_filho(self) -> Optional["EstadoBacktracking"]:
        possiveis = self._calcular_possiveis()
        if self.ordem_reversa:
            possiveis = list(reversed(possiveis))

        if self.logs:
            print(Fore.LIGHTBLACK_EX + f"Possíveis regras: {possiveis}" + Fore.RESET)

        
        if self.proxima_regra < len(possiveis):
            regra = possiveis[self.proxima_regra]
            self.proxima_regra += 1
            novo_baldes = self.baldes.clonar()
            getattr(novo_baldes, regra)()
            return EstadoBacktracking(pai=self, baldes=novo_baldes, regra_geradora=regra, ordem_reversa=self.ordem_reversa, logs=self.logs)

        self.impasse = True
        return None