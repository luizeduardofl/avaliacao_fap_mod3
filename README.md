# Sistema Bancário em Python

## Descrição do Projeto

Este é um sistema bancário simples desenvolvido em Python que utiliza o MySQL como banco de dados para armazenar e gerenciar informações sobre contas bancárias fictícias. Sua utilização é toda no terminal do sistema operacional. O sistema foi desenvolvido com o propósito de aprendizado e prática de conceitos de programação e banco de dados, mais especificamente, a integração entre Python e MySQL.

O sistema foi feito durante a FAP (Formação Acelerada em Programação) da SOFTEX Pernambuco.

## Vídeo Explicativo

Vídeo demonstrando o funcionamento do programa: https://youtu.be/fZ0XwFIDywY

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
```

---

### English Version

# Banking System in Python

## Project Description

This is a simple banking system developed in Python that uses MySQL as the database to store and manage information about fictitious bank accounts. It operates entirely in the operating system terminal. The system was created for learning purposes and to practice programming and database concepts, specifically the integration between Python and MySQL.

The system was created during the FAP (Accelerated Programming Training) at SOFTEX Pernambuco.

## Demo Video

Video demonstrating how the program works [in Portuguese]: https://youtu.be/fZ0XwFIDywY

## Features

- **Account Creation:** Allows the creation of new bank accounts with client data.
- **Deposit and Withdrawal:** Enables deposits and withdrawals from accounts.
- **Transfers:** Transfers between accounts registered in the system.
- **User Query:** Check the user’s name, balance, account creation date, and ID.
- **Statement:** Table of financial transactions, specifying the type of transaction and who performed it. Transactions are divided into three types:
  - 1 - deposit
  - 2 - withdrawal
  - 3 - transfer (both the sender and the receiver)

## Technologies Used

- **Language:** Python 3.9.13
- **Database:** MySQL
- **Libraries Used:**
  - `mysql.connector` (for connecting and manipulating the MySQL database)
  - `datetime` to capture the current date

## Prerequisites

Before starting, make sure you have the following installed:

- Python 3.9.13 or higher
- MySQL Server
- Required libraries (can be installed via `pip`):

```bash
pip install mysql-connector-python
```
