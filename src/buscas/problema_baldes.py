from typing import Optional

class ProblemaBaldes:

# OPERAÇÕES INTERNAS
    def __init__(self, baldes: Optional[list[int]] = None):
        self.baldes: list[int] = baldes if baldes is not None else [5, 0]

    def _get_b5(self) -> int:
        return self.baldes[0]

    def _get_b3(self) -> int:
        return self.baldes[1]

    def _set_b5(self, valor: int):
        if valor <= 5 or valor > 0:
            self.baldes[0] = valor

    def _set_b3(self, valor: int):
        if valor <= 3 or valor > 0:
            self.baldes[1] = valor

# OPERAÇÕES AUXILIARES
    def clonar(self) -> "ProblemaBaldes":
        return ProblemaBaldes(self.baldes.copy())

    def tupla(self) -> tuple[int, int]:
        return (self.baldes[0], self.baldes[1])

    def imprimir_baldes(self):
        print(f'BALDE MAIOR: {self.baldes[0]}')
        print(f'BALDE MENOR: {self.baldes[1]}')

    def is_solucionado(self) -> bool:
        return (self._get_b3() + self._get_b5()) == 4

# REGRAS DE TRANSIÇÃO
    def enche_b5(self):
        valor = self._get_b5()
        if valor >= 5:
            raise Exception("O balde maior já está cheio.")
        self._set_b5(5)

    def enche_b3(self):
        valor = self._get_b3()
        if valor >= 3:
            raise Exception("O balde menor já está cheio.")
        self._set_b3(3)

    def esvazia_b5(self) -> bool:
        valor = self._get_b5()
        if valor < 1:
            raise Exception("O balde maior já está vazio.")
        self._set_b5(0)
        return True

    def esvazia_b3(self):
        valor = self._get_b3()
        if valor < 1:
            raise Exception("O balde menor já está vazio.")
        self._set_b3(0)

    def b5_to_b3(self):
        valor_maior = self._get_b5()
        valor_menor = self._get_b3()

        if valor_maior == 0 or valor_menor >= 3:
            raise Exception("Não é possível transferir água do balde maior para o balde menor.")

        folga_menor = 3 - valor_menor
        if valor_maior <= folga_menor:
            self._set_b3(valor_menor + valor_maior)
            self._set_b5(0)
        else:
            self._set_b3(3)
            self._set_b5(valor_maior - folga_menor)

    def b3_to_b5(self) -> bool:
        valor_maior = self._get_b5()
        valor_menor = self._get_b3()

        if valor_menor == 0 or valor_maior >= 5:
            raise Exception("Não é possível transferir água do balde menor para o balde maior.")

        folga_maior = 5 - valor_maior
        if valor_menor <= folga_maior:
            self._set_b5(valor_menor + valor_maior)
            self._set_b3(0)
        else:
            self._set_b5(5)
            self._set_b3(valor_menor - folga_maior)
