# Processo de Desenvolvimento do Projeto "Calculadora de Gastos Mensais"

## Visão Geral
O objetivo deste projeto foi criar uma aplicação web simples para calcular gastos mensais, utilizando Python com Flask para o backend e HTML/CSS para a interface do usuário. O projeto foi desenvolvido em um ambiente Git, aproveitando branches para gerenciar diferentes partes do código.

---

## Estrutura do Projeto
- **Branch principal (main):** Contém o código estável e integrado.
- **Branches secundárias:**
  - `interface-usuario`: Para desenvolver a interface HTML e CSS.
  - `logica-backend`: Para implementar a lógica de cálculo no Flask.

---

## Passos do Desenvolvimento

### 1. Configuração Inicial
- Criamos a estrutura inicial do projeto:
- 
Para documentar o processo de desenvolvimento, você pode criar um arquivo chamado DEVELOPMENT.md no repositório e adicionar os detalhes sobre o que foi feito, os desafios enfrentados e como o Git ajudou no gerenciamento do projeto.

Exemplo de Arquivo DEVELOPMENT.md
markdown
Copiar código
# Processo de Desenvolvimento do Projeto "Calculadora de Gastos Mensais"

## Visão Geral
O objetivo deste projeto foi criar uma aplicação web simples para calcular gastos mensais, utilizando Python com Flask para o backend e HTML/CSS para a interface do usuário. O projeto foi desenvolvido em um ambiente Git, aproveitando branches para gerenciar diferentes partes do código.

---

## Estrutura do Projeto
- **Branch principal (main):** Contém o código estável e integrado.
- **Branches secundárias:**
  - `interface-usuario`: Para desenvolver a interface HTML e CSS.
  - `logica-backend`: Para implementar a lógica de cálculo no Flask.

---

## Passos do Desenvolvimento

### 1. Configuração Inicial
- Criamos a estrutura inicial do projeto:
Calculadora_gastos/ ├── app.py ├── templates/ │ └── index.html ├── static/ │ └── styles.css
- Configuramos o Git e vinculamos ao repositório remoto no GitHub.

### 2. Desenvolvimento por Branches
- **Interface do Usuário:**
- Branch: `interface-usuario`
- Implementamos o HTML para capturar os gastos do usuário.
- Adicionamos estilos básicos em `styles.css`.
- Commit e push da interface foram feitos separadamente.

- **Lógica do Backend:**
- Branch: `logica-backend`
- Desenvolvemos a lógica de cálculo de gastos no arquivo `app.py` usando Flask.
- Testamos a aplicação localmente para garantir que a funcionalidade estava correta.

### 3. Integração
- Mergemos as branches `interface-usuario` e `logica-backend` na branch principal (`main`).
- Resolvemos conflitos de forma eficiente usando as ferramentas do Git.

---

## Desafios Enfrentados
1. **Configuração do ambiente Flask:**
 - Inicialmente, houve dificuldades com a instalação do Flask e a execução do aplicativo.
 - Resolvemos isso configurando corretamente o ambiente virtual e instalando as dependências necessárias.

2. **Gerenciamento de Branches:**
 - Algumas branches não estavam conectadas ao repositório remoto.
 - Usamos o comando `git push --set-upstream` para corrigir.

3. **Integração de Código:**
 - Durante o merge, enfrentamos conflitos em arquivos compartilhados.
 - Utilizamos ferramentas de merge do VS Code para resolver.

---

## Como o Git Ajudou no Gerenciamento
- **Branches:** Permitiram trabalhar em diferentes partes do projeto simultaneamente sem interferências.
- **Commits:** Documentaram cada mudança no código, facilitando o rastreamento de problemas.
- **Push para GitHub:** Garantiu que o código estava sempre salvo e acessível remotamente.
- **Histórico de Versionamento:** Ajudou a recuperar versões antigas quando necessário.

---

## Próximos Passos
- Melhorar a interface do usuário com frameworks como Bootstrap.
- Adicionar novas funcionalidades, como a exportação dos dados para um arquivo CSV.

---

## Conclusão
O uso do Git foi fundamental para organizar o projeto, dividir tarefas e colaborar de maneira eficiente. Ele garantiu que todo o trabalho estivesse documentado e facilmente recuperável.

