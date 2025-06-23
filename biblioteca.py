import json
import os

ARQUIVO_BIBLIOTECA = "biblioteca.json"

LIVROS_INICIAIS = [
    "O Mágico de Oz",
    "O Poder do Hábito",
    "Orgulho e Preconceito",
    "Crime e Castigo",
    "Antifrágil",
    "Todos os Caminhos Levam a Roma",
    "A Branca de Neve",
    "Moby Dick"
]

def carregar_dados():
    if os.path.exists(ARQUIVO_BIBLIOTECA):
        try:
            with open(ARQUIVO_BIBLIOTECA, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Erro ao carregar os dados. O arquivo está corrompido. Inicializando novo inventário.")
    return {
        "livros_disponiveis": LIVROS_INICIAIS.copy(),
        "clientes": {}
    }

def salvar_dados(biblioteca):
    with open(ARQUIVO_BIBLIOTECA, "w", encoding="utf-8") as f:
        json.dump(biblioteca, f, ensure_ascii=False, indent=2)

def mostrar_livros(lista):
    for i, livro in enumerate(lista, 1):
        print(f"{i}. {livro}")

def obter_cpf():
    while True:
        cpf = input("Informe seu CPF (apenas números): ").strip()
        if cpf.isdigit() and len(cpf) >= 5:
            return cpf
        print("CPF inválido. Tente novamente.")

def obter_ou_cadastrar_usuario(cpf, biblioteca):
    clientes = biblioteca["clientes"]
    if cpf in clientes:
        return clientes[cpf]["nome"]
    nome = input("Primeiro acesso! Informe seu nome: ").strip()
    clientes[cpf] = {
        "nome": nome,
        "emprestimos": [],
        "historico": []
    }
    return nome

def emprestar_livro(cpf, biblioteca):
    livros = biblioteca["livros_disponiveis"]
    if not livros:
        print("Nenhum livro disponível no momento.")
        return

    print("\nLivros disponíveis:")
    mostrar_livros(livros)

    escolha = input("Digite o número do livro que deseja emprestar: ")
    if escolha.isdigit():
        idx = int(escolha) - 1
        if 0 <= idx < len(livros):
            livro = livros.pop(idx)
            cliente = biblioteca["clientes"][cpf]
            cliente["emprestimos"].append(livro)
            cliente["historico"].append(f"Emprestou: {livro}")
            print(f"Você emprestou: {livro}")
        else:
            print("Número inválido.")
    else:
        print("Entrada inválida.")

def devolver_livro(cpf, biblioteca):
    cliente = biblioteca["clientes"][cpf]
    emprestados = cliente["emprestimos"]

    if not emprestados:
        print("Você não possui livros emprestados.")
        return

    print("\nSeus livros emprestados:")
    mostrar_livros(emprestados)

    escolha = input("Digite o número do livro que deseja devolver: ")
    if escolha.isdigit():
        idx = int(escolha) - 1
        if 0 <= idx < len(emprestados):
            livro = emprestados.pop(idx)
            biblioteca["livros_disponiveis"].append(livro)
            cliente["historico"].append(f"Devolveu: {livro}")
            print(f"Você devolveu: {livro}")
        else:
            print("Número inválido.")
    else:
        print("Entrada inválida.")

def mostrar_historico(cpf, biblioteca):
    historico = biblioteca["clientes"][cpf]["historico"]
    if not historico:
        print("Você ainda não tem histórico.")
    else:
        print("\nHistórico de empréstimos/devoluções:")
        for evento in historico:
            print("-", evento)

def main():
    print("--- Bem-vindo à Biblioteca ---")
    biblioteca = carregar_dados()
    cpf = obter_cpf()
    nome = obter_ou_cadastrar_usuario(cpf, biblioteca)

    print(f"\nOlá, {nome}!")

    while True:
        print("\nO que deseja fazer?")
        print("1 - Emprestar livro")
        print("2 - Devolver livro")
        print("3 - Ver meu histórico")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            emprestar_livro(cpf, biblioteca)
        elif opcao == '2':
            devolver_livro(cpf, biblioteca)
        elif opcao == '3':
            mostrar_historico(cpf, biblioteca)
        elif opcao == '4':
            salvar_dados(biblioteca)
            print("Saindo. Dados salvos com sucesso.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
