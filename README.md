# DevQuest - TaskTracker Gamificado (CLI) 

O **DevQuest** é um sistema de gerenciamento de tarefas gamificado projetado para otimizar a rotina de estudos e entregas técnicas. A aplicação combate a procrastinação, a sobrecarga mental e a falta de priorização ao transformar o acompanhamento de demandas em uma jornada interativa de RPG: cada tarefa cadastrada torna-se uma **Missão (Quest)** que concede Pontos de Experiência (XP) atrelados ao seu nível de prioridade. 
--- 
## Problema e Solução 
- **O Problema**: Listas de tarefas estáticas e convencionais costumam ser pouco engajadoras, levando à perda de foco, desorganização diante de múltiplos prazos e falta de clareza sobre quais tarefas geram maior impacto.
- **A Solução**: O DevQuest traz dinamismo e feedback imediato. Ao cadastrar e visualizar suas missões em um terminal interativo, a pessoa usuária ganha clareza de suas prioridades e acompanha seu acúmulo de XP em tempo real.
---
## Regras de Negócio e Sistema de XP 
- **Validação de Título**: O título da missão é estritamente obrigatório. O sistema rejeita campos vazios ou preenchidos apenas com espaços.
- **Prioridades Válidas**: Aceita exclusivamente as categorias `Baixa`, `Média` (ou `Media`) e `Alta`.
- **Atribuição Automática de XP**:
- - **Prioridade Baixa**: **+10 XP**
- - **Prioridade Média**: **+25 XP**
- - **Prioridade Alta**: **+50 XP**
- **Status Inicial**: Toda nova missão cadastrada recebe automaticamente o status **Pendente**.
- **Cálculo de Nível**: A cada **200 XP** acumulados, o jogador avança para um novo nível no sistema.
---
## Tecnologias Utilizadas 
- **Linguagem**: Python 3.12+
- **Interface**: CLI (Interface de Linha de Comando)
- **Controle de Versão**: Git &amp; GitHub
---
## Estrutura do Repositório 
```
plaintext devquest-tasktracker
├── README.md # Documentação principal do projeto
├── .gitignore # Arquivo de regras para ignorar temporários do Python
├── docs
│   └── planejamento\_logico\_devquest.pdf # Documento de planejamento da Fase 1
└── src
    └── main.py # Código-fonte principal da aplicação CLI em Python
```
* **Gabrielle Keiko**
* Aluna de Ciência de Dados e Machine Learning no **CEUB**
* Business Intelligence 2026
* E-mail institucional: [gabrielle.keiko@sempreceub.com](mailto:gabrielle.keiko@sempreceub.com) | E-mail pessoal: [gkeiko.05@gmail.com](mailto:gkeiko.05@gmail.com)
* Meu Perfil no LinkedIn: [Gabrielle Keiko](https://www.linkedin.com/in/gabrielle-keiko-9baa6a2b3/)
