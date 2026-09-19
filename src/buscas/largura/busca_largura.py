from collections import deque
from ..problema_baldes import ProblemaBaldes
from .estado_largura import EstadoLargura
from colorama import Fore

class BuscaLargura:
    def __init__(self, ordem_reversa: bool = False, logs: bool = False):
        self.baldes = ProblemaBaldes()
        self.ordem_reversa = ordem_reversa
        self.logs = logs
        self.impasses = 0
        self.solucao: EstadoLargura | None = None

        estado_raiz = EstadoLargura(pai=None, baldes=self.baldes, ordem_reversa=ordem_reversa, logs=logs)

        self.abertos = deque([estado_raiz])

        self.visitados = {self.baldes.tupla()}

    def busca_completa(self) -> bool:
        while self.abertos:
            estado_atual = self.abertos.popleft()

            if self.logs:
                print(f'---------- NÍVEL {estado_atual.nivel} ---------')
                print(Fore.LIGHTBLACK_EX + f'Explorando: {estado_atual.baldes.tupla()}' + Fore.RESET)

            if estado_atual.baldes.is_solucionado():
                self.solucao = estado_atual
                return True

            filhos = estado_atual.gerar_filhos()

            if not filhos:
                self.impasses += 1
                if self.logs:
                    print(Fore.RED + f'Estado {estado_atual.baldes.tupla()} é um impasse (sem filhos válidos).' + Fore.RESET)
                continue

            for filho in filhos:
                chave = filho.baldes.tupla()
                if chave not in self.visitados:
                    self.visitados.add(chave)
                    self.abertos.append(filho)
                    if self.logs:
                        print(Fore.GREEN + f'Regra {filho.regra_geradora} aplicada. Estado {chave} entra na fila de abertos.' + Fore.RESET)
                else:
                    if self.logs:
                        print(Fore.MAGENTA + f'Estado {chave} já visitado. Descartando.' + Fore.RESET)

        return False

    def imprime_solucao(self):
        if self.solucao is None:
            print(Fore.RED + "Nenhuma solução encontrada para imprimir." + Fore.RESET)
            return

        caminho = []
        estado = self.solucao
        while estado is not None:
            caminho.append(estado)
            estado = estado.pai
        caminho.reverse()

        for i, estado in enumerate(caminho):
            print(f'------ Passo {i} ------')
            estado.baldes.imprimir_baldes()
            print(f'Regra aplicada: {estado.regra_geradora}')