from typing import Optional

class ProblemaBaldes:

# OPERAÇÕES INTERNAS
    def __init__(self, baldes: Optional[list[int]] = None):
        self.baldes: list[int] = baldes if baldes is not None else [5, 0]

    def _get_b5(self) -> int:
        return self.baldes[0]

    def _get_b3(self) -> int:
        return self.baldes[1]

    def _set_b5(self, valor: int) -> bool:
        if valor > 5 or valor < 0:
            return False
        self.baldes[0] = valor
        return True

    def _set_b3(self, valor: int) -> bool:
        if valor > 3 or valor < 0:
            return False
        self.baldes[1] = valor
        return True

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
            raise ValueError("O balde maior já está cheio.")
        self._set_b5(5)

    def enche_b3(self) -> bool:
        valor = self._get_b3()
        if valor >= 3:
            return False
        self._set_b3(3)
        return True

    def esvazia_b5(self) -> bool:
        valor = self._get_b5()
        if valor < 1:
            return False
        self._set_b5(0)
        return True

    def esvazia_b3(self) -> bool:
        valor = self._get_b3()
        if valor < 1:
            return False
        self._set_b3(0)
        return True

    def b5_to_b3(self) -> bool:
        valor_maior = self._get_b5()
        valor_menor = self._get_b3()

        if valor_maior == 0 or valor_menor >= 3:
            return False

        folga_menor = 3 - valor_menor
        if valor_maior <= folga_menor:
            self._set_b3(valor_menor + valor_maior)
            self._set_b5(0)
        else:
            self._set_b3(3)
            self._set_b5(valor_maior - folga_menor)
        return True

    def b3_to_b5(self) -> bool:
        valor_maior = self._get_b5()
        valor_menor = self._get_b3()

        if valor_menor == 0 or valor_maior >= 5:
            return False

        folga_maior = 5 - valor_maior
        if valor_menor <= folga_maior:
            self._set_b5(valor_menor + valor_maior)
            self._set_b3(0)
        else:
            self._set_b5(5)
            self._set_b3(valor_menor - folga_maior)
        return True