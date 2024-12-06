# Calculadora de Gastos Mensais

## Objetivo do Projeto

O objetivo deste projeto é desenvolver uma **aplicação web** simples usando **Flask** para calcular e controlar os gastos mensais de um usuário. A aplicação permitirá que os usuários insiram suas despesas e categorizem-nas, facilitando a visualização e o planejamento de suas finanças.

---

## Funcionalidades Planejadas

1. **Tela Inicial (Home)**:
   - Exibir um formulário para o usuário inserir suas despesas mensais, incluindo categoria (ex: alimentação, transporte, lazer), valor e descrição.
   
2. **Listagem de Despesas**:
   - Exibir as despesas registradas em uma tabela.
   - Permitir a visualização dos gastos totais por categoria.

3. **Resumo de Gastos**:
   - Mostrar o valor total de despesas do mês.
   - Exibir um gráfico de barras ou pizza para ilustrar a distribuição dos gastos por categoria.

4. **Edição e Exclusão de Despesas**:
   - Permitir que o usuário edite ou remova uma despesa já registrada.

5. **Persistência de Dados**:
   - Usar uma solução de banco de dados simples (como SQLite) para armazenar as despesas.

6. **Interface Responsiva**:
   - A interface será responsiva, permitindo o uso da aplicação em dispositivos móveis.

---

## Cronograma de Desenvolvimento

### Etapa 1: Planejamento e Estruturação do Projeto (1 dia)
- Definição de requisitos e funcionalidades.
- Criação da estrutura de diretórios do projeto.
- Instalação e configuração do Flask.

### Etapa 2: Implementação da Tela Inicial e Formulário de Entrada (2 dias)
- Desenvolver o formulário para inserção de despesas.
- Criar as rotas no Flask para exibir a tela inicial e processar as entradas.

### Etapa 3: Listagem de Despesas (2 dias)
- Criar a funcionalidade de exibição das despesas registradas.
- Implementar a estrutura da tabela para visualizar os gastos.

### Etapa 4: Resumo de Gastos e Gráficos (3 dias)
- Implementar a funcionalidade de resumo de gastos (total por categoria e total geral).
- Integrar gráficos utilizando uma biblioteca como o **Chart.js** ou **Plotly**.

### Etapa 5: Edição e Exclusão de Despesas (2 dias)
- Implementar as funcionalidades para editar e excluir uma despesa existente.
  
### Etapa 6: Persistência de Dados (2 dias)
- Configurar e integrar o banco de dados **SQLite** para armazenar as despesas.
- Implementar a persistência de dados ao longo das sessões do usuário.

### Etapa 7: Testes e Documentação (1 dia)
- Realizar testes manuais para garantir o funcionamento da aplicação.
- Criar a documentação e o arquivo **README.md**.

### Etapa 8: Implementação de Melhorias e Feedback (2 dias)
- Revisão do código e implementações com base no feedback.
- Melhoria da interface e da experiência do usuário.

---

## Como Rodar o Projeto

1. **Clone o repositório**:
   ```bash