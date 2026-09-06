from src.buscas.backtracking.busca_backtracking import BuscaBacktracking
from colorama import Fore

if __name__ == "__main__":

    busca = input("Qual busca deseja executar?\n1 - Busca Backtracking\n2 - Busca em Profundidade\n3 - Busca em Profundidade\n4 - Busca Ordenada\n5 - Busca Gulosa\n6 - Busca A*\n0 - Sair\n").strip()

    match busca:
        case "1":
            ordem = input("Deseja executar a busca em que ordem?:\nA - Crescente\nB - Decrescente\n").strip().lower()

            match ordem:
                case "a":
                    is_ordem_reversa = False
                case "b":
                    is_ordem_reversa = True
                case _:
                    print(Fore.RED + "Opção inválida. Encerrando o programa." + Fore.RESET)
                    exit(0)

            logs = input("Deseja exibir logs detalhados da execução? (s/n): ").strip().lower()
            
            is_logs = logs == 's'

            if is_logs:
                print("----- EXECUTANDO BUSCA -----")

            busca = BuscaBacktracking(ordem_reversa=is_ordem_reversa, logs=is_logs)
            if busca.busca_completa():
                print(Fore.GREEN + "--- Solução encontrada! ---" + Fore.RESET)
                print(Fore.RED + f"Total de impasses encontrados: {busca.impasses}" + Fore.RESET)

                imprimir_solucao = input("Deseja imprimir a solução encontrada? (s/n): ").strip().lower()
                if imprimir_solucao == 's':
                    busca.imprime_solucao()
            else:
                print(Fore.RED + "Não foi possível encontrar solução (impasse)." + Fore.RESET)

        case "2":
            print(Fore.RED + "Busca em Profundidade ainda não implementada." + Fore.RESET)

        case "3":
            print(Fore.RED + "Busca em Largura ainda não implementada." + Fore.RESET)

        case "4":
            print(Fore.RED + "Busca Ordenada ainda não implementada." + Fore.RESET)

        case "5":
            print(Fore.RED + "Busca Gulosa ainda não implementada." + Fore.RESET)

        case "6":
            print(Fore.RED + "Busca A* ainda não implementada." + Fore.RESET) 

        case "0":
            print(Fore.RED + "Encerrando o programa." + Fore.RESET)
        
        case _:
            print(Fore.RED + "Opção inválida. Encerrando o programa." + Fore.RESET)