from src.buscas.backtracking.busca_backtracking import BuscaBacktracking

if __name__ == "__main__":
    busca = BuscaBacktracking()
    if busca.busca_completa():
        print("Solução encontrada!\n")
        busca.imprime_solucao()
    else:
        print("Não foi possível encontrar solução (impasse).")