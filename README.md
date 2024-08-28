# Sistema Bancário em Python

## Descrição do Projeto

Este é um sistema bancário simples desenvolvido em Python que utiliza o MySQL como banco de dados para armazenar e gerenciar informações sobre contas bancárias fictícias. Sua utilização é toda no terminal do sistema operacional. O sistema foi desenvolvido com o propósito de aprendizado e prática de conceitos de programação e banco de dados, mais especificamente, a integração entre Python e MySQL.

O sistema foi feito durante a FAP (Formação Acelerada em Programação) da SOFTEX Pernambuco.

## Funcionalidades

- **Criação de Contas Bancárias:** Possibilita criar novas contas bancárias com dados de clientes.
- **Depósito e Saque:** Permite a realização de depósitos e saques nas contas.
- **Transferências:** Transferências entre contas cadastradas no sistema.
- **Consulta de Usuário:** Verificar o nome do usuário, seu saldo, data de criação da conta e id.
- **Extrato:** Tabela de movimentações financeiras, explicitando o tipo da movimentação e quem a fez. São divididas em três tipos:
  - 1 - depósito
  - 2 - saque
  - 3 - transferência (tanto de quem a realiza quanto de quem a recebe)

## Tecnologias Utilizadas

- **Linguagem:** Python 3.9.13
- **Banco de Dados:** MySQL
- **Bibliotecas Utilizadas:**
  - `mysql.connector` (para a conexão e manipulação do banco de dados MySQL)
  - `datetime` para capturar a data atual

## Pré-requisitos

Antes de iniciar, certifique-se de ter o seguinte instalado:

- Python 3.9.13 ou superior
- MySQL Server
- Bibliotecas necessárias (pode ser instalado via `pip`):

```bash
pip install mysql-connector-python
