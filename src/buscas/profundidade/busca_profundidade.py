from ..problema_baldes import ProblemaBaldes
from .estado_profundidade import EstadoProfundidade
from colorama import Fore

class BuscaProfundidade:
    def __init__(self, ordem_reversa: bool = False, logs: bool = False, limite_profundidade: int = 50):
        self.baldes = ProblemaBaldes()
        self.ordem_reversa = ordem_reversa
        self.logs = logs
        self.limite_profundidade = limite_profundidade
        self.impasses = 0
        self.solucao: EstadoProfundidade | None = None

        estado_raiz = EstadoProfundidade(pai=None, baldes=self.baldes, ordem_reversa=ordem_reversa, logs=logs)

        # Usamos uma lista Python comum como Pilha (LIFO)
        self.abertos = [estado_raiz]
        self.visitados = {self.baldes.tupla()}

    def busca_completa(self) -> bool:
        while self.abertos:
            # LIFO: remove o último elemento inserido (topo da pilha)
            estado_atual = self.abertos.pop()

            if self.logs:
                print(f'---------- NÍVEL {estado_atual.nivel} ---------')
                print(Fore.LIGHTBLACK_EX + f'Explorando: {estado_atual.baldes.tupla()}' + Fore.RESET)

            if estado_atual.baldes.is_solucionado():
                self.solucao = estado_atual
                return True

            # Trava para evitar estouro/loop infinito em caminhos muito profundos
            if estado_atual.nivel >= self.limite_profundidade:
                self.impasses += 1
                if self.logs:
                    print(Fore.RED + f'Limite de profundidade ({self.limite_profundidade}) atingido em {estado_atual.baldes.tupla()}. Voltando...' + Fore.RESET)
                continue

            filhos = estado_atual.gerar_filhos()

            if not filhos:
                self.impasses += 1
                if self.logs:
                    print(Fore.RED + f'Estado {estado_atual.baldes.tupla()} é um impasse (sem filhos válidos).' + Fore.RESET)
                continue

            # Invertemos a ordem dos filhos ao empilhar para que o primeiro filho gerado
            # fique no topo e seja explorado antes dos seus irmãos.
            novos_nos = 0
            for filho in reversed(filhos):
                chave = filho.baldes.tupla()
                if chave not in self.visitados:
                    self.visitados.add(chave)
                    self.abertos.append(filho)
                    novos_nos += 1
                    if self.logs:
                        print(Fore.GREEN + f'Regra {filho.regra_geradora} aplicada. Estado {chave} empilhado.' + Fore.RESET)
                else:
                    if self.logs:
                        print(Fore.MAGENTA + f'Estado {chave} já visitado. Descartando.' + Fore.RESET)

            if novos_nos == 0:
                self.impasses += 1

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