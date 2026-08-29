from ..problema_baldes import ProblemaBaldes
from .estado_backtracking import EstadoBacktracking

class BuscaBacktracking:
    def __init__(self):
        self.baldes = ProblemaBaldes()
        self.nivel = 0
        self.estados = [EstadoBacktracking(pai=None, baldes=self.baldes)]
        self.visitados = {self.baldes.tupla()}

    def print(self):
        self.estados[self.nivel].baldes.print()

    def busca_completa(self) -> bool:
        while not self.estados[self.nivel].baldes.is_solucionado():
            estado_atual = self.estados[self.nivel]
            novo_estado = estado_atual.gerar_filho()

            if novo_estado is not None:
                chave = (novo_estado.baldes.tupla())
                if chave not in self.visitados:
                    self.visitados.add(chave)
                    self.nivel += 1
                    self.estados.append(novo_estado)
            else:
                if self.nivel == 0:
                    return False
                self.estados.pop()
                self.nivel -= 1

        return True

    def imprime_solucao(self):
        caminho = []
        estado = self.estados[self.nivel]
        while estado is not None:
            caminho.append(estado)
            estado = estado.pai
        caminho.reverse()

        for i, estado in enumerate(caminho):
            print(f'--- Passo {i} ---')
            estado.baldes.print()