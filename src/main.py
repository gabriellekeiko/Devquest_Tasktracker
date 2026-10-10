import sys


def exibir_menu():
    """Exibe o menu principal de navegação contínua da aplicação CLI."""
    print("\n" + "=" * 50)
    print("⚔️ DEVQUEST - TASKTRACKER GAMIFICADO (CLI) ⚔️")
    print("1. Cadastrar nova missão")
    print("2. Visualizar missões cadastradas")
    print("3. Sair")
    print("=" * 50)


def cadastrar_missao(missoes):
    """
    Cadastra uma missão na lista, aplicando validações de título e prioridade,
    e calculando a recompensa em XP.
    """
    print("\n--- CADASTRO DE NOVA MISSÃO ---")

    while True:
        titulo = input("Digite o título da missão: ").strip()
        if titulo:
            break
        print("❌ Erro: O título da missão é obrigatório e não pode ficar em branco!")

    descricao = input("Digite a descrição da missão (opcional): ").strip()
    if not descricao:
        descricao = "Sem descrição fornecida."

    prioridades_validas = {
        "alta": "Alta",
        "media": "Média",
        "média": "Média",
        "baixa": "Baixa",
    }

    while True:
        prioridade_input = input("Digite a prioridade da missão (Alta, Média, Baixa): ").strip().lower()
        if prioridade_input in prioridades_validas:
            prioridade = prioridades_validas[prioridade_input]
            break
        print("❌ Erro: Prioridade inválida! Digite apenas 'Alta', 'Média' ou 'Baixa'.")

    data_limite = input("Digite a data limite da missão (formato: DD/MM/AAAA): ").strip()
    if not data_limite:
        data_limite = "Não especificada"

    xp_por_prioridade = {
        "Alta": 100,
        "Média": 50,
        "Baixa": 20,
    }

    xp_ganho = xp_por_prioridade[prioridade]

    nova_missao = {
        "id": len(missoes) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "xp_ganho": xp_ganho,
        "status": "Pendente",
    }

    missoes.append(nova_missao)
    print(f"✅ Missão '{titulo}' cadastrada com sucesso! Recompensa: {xp_ganho} XP.")


def visualizar_missoes(missoes):
    """
    Exibe todas as missões cadastradas, detalhando título, descrição,
    prioridade, data limite, status e XP ganho.
    """
    if not missoes:
        print("\n⚠️ Nenhuma missão cadastrada no momento.")
        return

    xp_total_pendente = 0

    print("\n--- MISSÕES CADASTRADAS ---")

    for idx, m in enumerate(missoes, start=1):
        if m["status"] == "Pendente":
            xp_total_pendente += m["xp_ganho"]

        print(f"\n[--- MISSÃO {idx} ---] {m['titulo']}")
        print(f"Descrição: {m['descricao']}")
        print(f"Prioridade: {m['prioridade']} ({m['xp_ganho']} XP)")
        print(f"Data Limite: {m['data_limite']}")
        print(f"Status: {m['status']}")
        print("-" * 50)

    print(f"\n📊 XP Total de Missões Pendentes: {xp_total_pendente} XP")
    print(f"🔮 XP Total acumulado em jogo: {xp_total_pendente} XP")


def main():
    """Loop principal da aplicação CLI."""
    missoes = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            cadastrar_missao(missoes)
        elif opcao == "2":
            visualizar_missoes(missoes)
        elif opcao == "3":
            print("\nEncerrando o DevQuest... Até a próxima jornada! 🚀")
            sys.exit(0)
        else:
            print("❌ Opção inválida! Por favor, escolha entre 1, 2 ou 3.")


if __name__ == "__main__":
    main()