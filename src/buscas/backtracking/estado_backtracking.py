from typing import Optional
from ..problema_baldes import ProblemaBaldes

class EstadoBacktracking:

    ORDEM_EXECUCAO = [
        "enche_b3",
        "enche_b5",
        "esvazia_b3",
        "esvazia_b5",
        "b3_to_b5",
        "b5_to_b3",
    ]
    
    def __init__(self, pai: Optional["EstadoBacktracking"] = None, baldes: ProblemaBaldes = None):
        self.baldes = baldes if baldes else ProblemaBaldes()
        self.pai = pai
        self.proxima_regra = 0
        self.impasse = False
      
    def gerar_filho(self):
        while self.proxima_regra < len(self.ORDEM_EXECUCAO):
            nome_regra = self.ORDEM_EXECUCAO[self.proxima_regra]
            self.proxima_regra += 1
            
            candidato_baldes = self.baldes.clonar()
            try:
                getattr(candidato_baldes, nome_regra)()
                return EstadoBacktracking(pai=self, baldes=candidato_baldes)
            except Exception:
                print(f"Regra {nome_regra} não pôde ser aplicada.")
        self.impasse = True
        return None