from typing import Optional
from ..problema_baldes import ProblemaBaldes

class EstadoBacktracking:

    ORDEM_EXECUCAO = [
        "regra_5",
        "regra_2",
        "regra_4",
        "regra_3",
        "regra_1",
        "regra_6",
    ]
    
    def __init__(self, pai: Optional["EstadoBacktracking"] = None, baldes: ProblemaBaldes = None):
        self.baldes = baldes if baldes else ProblemaBaldes()
        self.pai = pai
        self.proxima_regra = 0
        self.impasse = False
        self.regras = {
            "regra_1": self.baldes.enche_balde_menor,
            "regra_2": self.baldes.enche_balde_maior,
            "regra_3": self.baldes.esvazia_balde_menor,
            "regra_4": self.baldes.esvazia_balde_maior,
            "regra_5": self.baldes.balde_menor_to_balde_maior,
            "regra_6": self.baldes.balde_maior_to_balde_menor,
        }
        

    def gerar_filho(self):
        while self.proxima_regra < len(self.ORDEM_EXECUCAO):
            nome_regra = self.ORDEM_EXECUCAO[self.proxima_regra]
            self.proxima_regra += 1
            
            candidato = EstadoBacktracking(pai=self, baldes=self.baldes.clonar())
            if candidato.regras[nome_regra]():
                return candidato
        self.impasse = True
        return None