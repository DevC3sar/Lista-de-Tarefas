# main.py
from tarefas import Tarefas

def main():
    lista_de_tarefas = Tarefas()

    while True:
        print("\n### Lista de Tarefas ###")
        print("1. Adicionar Tarefa")
        print("2. Marcar Tarefa como Concluída")
        print("3. Listar Tarefas")
        print("4. Remover Tarefa")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            descricao = input("Digite a descrição da tarefa: ")
            lista_de_tarefas.adicionar_tarefa(descricao)
        elif escolha == "2":
            lista_de_tarefas.listar_tarefas()
            indice = int(input("Digite o índice da tarefa concluída: "))
            lista_de_tarefas.marcar_como_concluida(indice)
        elif escolha == "3":
            lista_de_tarefas.listar_tarefas()
        elif escolha == "4":
            lista_de_tarefas.listar_tarefas()
            indice = int(input("Digite o índice da tarefa a ser removida: "))
            lista_de_tarefas.remover_tarefa(indice)
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
