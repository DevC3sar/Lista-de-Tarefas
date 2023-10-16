# tarefas.py
class Tarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        self.tarefas.append({"descricao": descricao, "concluida": False})
        print("Tarefa adicionada com sucesso!")

    def marcar_como_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Índice inválido.")

    def listar_tarefas(self):
        print("\n### Lista de Tarefas ###")
        for i, tarefa in enumerate(self.tarefas):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i}. [{status}] {tarefa['descricao']}")

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
            print("Tarefa removida com sucesso!")
        else:
            print("Índice inválido.")
