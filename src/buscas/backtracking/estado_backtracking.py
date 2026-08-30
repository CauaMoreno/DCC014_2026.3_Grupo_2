from typing import Optional
from ..problema_baldes import ProblemaBaldes

class EstadoBacktracking:

    ORDEM_EXECUCAO = [
        "enche_balde_menor",
        "enche_balde_maior",
        "esvazia_balde_menor",
        "esvazia_balde_maior",
        "balde_menor_to_balde_maior",
        "balde_maior_to_balde_menor",
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
            if getattr(candidato_baldes, nome_regra)():
                return EstadoBacktracking(pai=self, baldes=candidato_baldes)
            
        self.impasse = True
        return None