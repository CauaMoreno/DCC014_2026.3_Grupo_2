from ..problema_baldes import ProblemaBaldes
from .estado_backtracking import EstadoBacktracking
from colorama import Fore

class BuscaBacktracking:
    def __init__(self, ordem_reversa: bool = False, logs: bool = False):
        self.baldes = ProblemaBaldes()
        self.nivel = 0
        self.estados = [EstadoBacktracking(pai=None, baldes=self.baldes, ordem_reversa=ordem_reversa, logs=logs)]
        self.visitados = {self.baldes.tupla()}
        self.ordem_reversa = ordem_reversa
        self.impasses = 0
        self.logs = logs

    def busca_completa(self) -> bool:
        while not self.estados[self.nivel].baldes.is_solucionado():
            if self.logs:
                print(f'---------- NÍVEL {self.nivel} ---------')
 
            if self.nivel > 10:
                if self.logs:
                    print(Fore.RED + f'Nível muito profundo. Voltando para o nível {self.nivel - 1}..' + Fore.RESET)

                self.estados.pop()
                self.nivel -= 1
                self.impasses += 1

                continue

            estado_atual = self.estados[self.nivel]
            if self.logs:
                print(Fore.LIGHTBLACK_EX + f'Baldes: {estado_atual.baldes.tupla()}' + Fore.RESET)

            novo_estado = estado_atual.gerar_filho()

            if novo_estado is not None:
                chave = (novo_estado.baldes.tupla())

                if self.logs:
                    print(Fore.LIGHTBLACK_EX + f'Tentando aplicar regra: {novo_estado.regra_geradora}' + Fore.RESET)
                
                if chave not in self.visitados:
                    self.visitados.add(chave)
                    self.nivel += 1
                    self.estados.append(novo_estado)
                    if self.logs:
                        print(Fore.GREEN + f'Regra aplicada com sucesso. Avançando para o nível {self.nivel}.' + Fore.RESET)
                else:
                    if self.logs:
                        print(Fore.MAGENTA + f'Estado {novo_estado.baldes.tupla()} já visitado. Tentando próxima regra.' + Fore.RESET)
            else:
                if self.nivel == 0:
                    return False
                
                if self.logs:
                    print(Fore.RED + f'Impasse no nível {self.nivel}. Voltando para o nível {self.nivel - 1}.' + Fore.RESET)
                
                self.estados.pop()
                self.nivel -= 1
                self.impasses += 1

        return True

    def imprime_solucao(self):
        caminho = []
        estado = self.estados[self.nivel]
        while estado is not None:
            caminho.append(estado)
            estado = estado.pai
        caminho.reverse()

        for i, estado in enumerate(caminho):
            print(f'------ Passo {i} ------')
            estado.baldes.imprimir_baldes()
            print(f'Regra aplicada: {estado.regra_geradora}')