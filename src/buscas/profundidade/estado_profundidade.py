from typing import Optional
from ..problema_baldes import ProblemaBaldes
from colorama import Fore

class EstadoProfundidade:

    REGRAS = [
        "enche_b3",
        "enche_b5",
        "esvazia_b3",
        "esvazia_b5",
        "b3_to_b5",
        "b5_to_b3",
    ]

    def __init__(self, pai: Optional["EstadoProfundidade"] = None, baldes: ProblemaBaldes = None,
                 regra_geradora: Optional[str] = None, ordem_reversa: bool = False, logs: bool = False):
        self.baldes = baldes if baldes else ProblemaBaldes()
        self.pai = pai
        self.regra_geradora = regra_geradora
        self.ordem_reversa = ordem_reversa
        self.logs = logs

        self.nivel = 0 if pai is None else pai.nivel + 1

    def gerar_filhos(self) -> list["EstadoProfundidade"]:
        ordem = list(reversed(self.REGRAS)) if self.ordem_reversa else self.REGRAS

        filhos = []
        for nome_regra in ordem:
            candidato_baldes = self.baldes.clonar()
            try:
                getattr(candidato_baldes, nome_regra)()
            except Exception:
                continue

            filhos.append(EstadoProfundidade(
                pai=self,
                baldes=candidato_baldes,
                regra_geradora=nome_regra,
                ordem_reversa=self.ordem_reversa,
                logs=self.logs,
            ))

        if self.logs:
            regras_geradas = [f.regra_geradora for f in filhos]
            print(Fore.LIGHTBLACK_EX + f"Filhos válidos gerados: {regras_geradas}" + Fore.RESET)

        return filhos