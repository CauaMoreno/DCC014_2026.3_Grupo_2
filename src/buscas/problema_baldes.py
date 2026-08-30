from typing import Optional

class ProblemaBaldes:

# OPERAÇÕES INTERNAS
    def __init__(self, baldes: Optional[list[int]] = None):
        self.baldes: list[int] = baldes if baldes is not None else [5, 0]

    def _get_balde_maior(self) -> int:
        return self.baldes[0]

    def _get_balde_menor(self) -> int:
        return self.baldes[1]

    def _set_balde_maior(self, valor: int) -> bool:
        if valor > 5 or valor < 0:
            return False
        self.baldes[0] = valor
        return True

    def _set_balde_menor(self, valor: int) -> bool:
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
        return (self._get_balde_menor() + self._get_balde_maior()) == 4

# REGRAS DE TRANSIÇÃO
    def enche_balde_maior(self) -> bool:
        valor = self._get_balde_maior()
        if valor >= 5:
            return False
        self._set_balde_maior(5)
        return True

    def enche_balde_menor(self) -> bool:
        valor = self._get_balde_menor()
        if valor >= 3:
            return False
        self._set_balde_menor(3)
        return True

    def esvazia_balde_maior(self) -> bool:
        valor = self._get_balde_maior()
        if valor < 1:
            return False
        self._set_balde_maior(0)
        return True

    def esvazia_balde_menor(self) -> bool:
        valor = self._get_balde_menor()
        if valor < 1:
            return False
        self._set_balde_menor(0)
        return True

    def balde_maior_to_balde_menor(self) -> bool:
        valor_maior = self._get_balde_maior()
        valor_menor = self._get_balde_menor()

        if valor_maior == 0 or valor_menor >= 3:
            return False

        folga_menor = 3 - valor_menor
        if valor_maior <= folga_menor:
            self._set_balde_menor(valor_menor + valor_maior)
            self._set_balde_maior(0)
        else:
            self._set_balde_menor(3)
            self._set_balde_maior(valor_maior - folga_menor)
        return True

    def balde_menor_to_balde_maior(self) -> bool:
        valor_maior = self._get_balde_maior()
        valor_menor = self._get_balde_menor()

        if valor_menor == 0 or valor_maior >= 5:
            return False

        folga_maior = 5 - valor_maior
        if valor_menor <= folga_maior:
            self._set_balde_maior(valor_menor + valor_maior)
            self._set_balde_menor(0)
        else:
            self._set_balde_maior(5)
            self._set_balde_menor(valor_menor - folga_maior)
        return True