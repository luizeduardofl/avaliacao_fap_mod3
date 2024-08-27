import datetime
import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'minha_senha_banco',
    database = 'banco_fap',
    port = '3306'
)
cursor = conexao.cursor()

presente = datetime.datetime.now().date()

print('Seja bem-vindo ao Banco FAP.')

while True:
    print()
    print('Que área você gostaria de acessar?')
    print('1. Área do cliente')
    print('2. Área do gerente')
    print('3. Sair')
    comando = int(input())
    if comando == 1:

        print('______________ÁREA DO CLIENTE_____________')
        print()
        print('O que deseja fazer? ')
        print('1. Criar conta')
        print('2. Fazer depósito')
        print('3. Fazer saque')
        print('4. Dados de conta')
        print('5. Sair')

        comando = int(input())
        if comando == 1:
            nome = input('Digite seu nome: ').title()

            comando_sql = f'INSERT INTO contas (nome_conta, data_criacao, saldo_conta) VALUES ("{nome}", "{presente}", {0})'
            cursor.execute(comando_sql)
            conexao.commit()

            print('Conta cadastrada com sucesso.')

        if comando == 2:
            numero_conta = int(input('Número da conta: '))
            quantia_depositada = int(input('Quantia a ser depositada: '))

            comando_sql = f'SELECT saldo_conta FROM contas WHERE id_conta = {numero_conta}'
            cursor.execute(comando_sql)
            resultado = cursor.fetchall()

            saldo_atual = resultado[0][0]
            novo_saldo = saldo_atual + quantia_depositada

            comando_sql = f'UPDATE contas SET saldo_conta = {novo_saldo} WHERE id_conta = {numero_conta}'
            cursor.execute(comando_sql)

            conexao.commit()

            print('Depósito realizado com sucesso.') 

        if comando == 3:
            numero_conta = int(input('Número da conta: '))
            quantia_sacada = int(input('Quantia a ser sacada: '))

            comando_sql = f'SELECT saldo_conta FROM contas WHERE id_conta = {numero_conta}'
            cursor.execute(comando_sql)
            resultado = cursor.fetchall()

            saldo_atual = resultado[0][0] 

            if saldo_atual >= quantia_sacada:
                novo_saldo = saldo_atual - quantia_sacada
                comando_sql = f'UPDATE contas SET saldo_conta = {novo_saldo} WHERE id_conta = {numero_conta}'
                cursor.execute(comando_sql)
                conexao.commit()
                print('Saque realizado com sucesso. ')
            else:
                print(f'Comando inválido. Saldo insuficiente. Saldo atual: {saldo_atual}')

        if comando == 4:
            numero_conta = int(input('Número da conta: '))
            comando_sql = f'SELECT * FROM contas WHERE id_conta = {numero_conta}'
            cursor.execute(comando_sql)
            resultado = cursor.fetchall()
            print(resultado)

        if comando == 5:
            cursor.close()
            conexao.close() 
            break
    elif comando == 2:
        print('______________ÁREA DO GERENTE_____________')
        print()
        print('O que deseja fazer? ')
        print('1. Edição de conta')
        print('2. Exclusão de conta')
        print('3. Exibir todas as contas')
        print('4. Sair')
        comando = int(input())
        if comando == 1:
            print('___________________________')
            numero_conta = int(input('Número da conta: '))
            
            novo_nome = input('Novo nome (deixe-o em branco para mantê-lo inalterado): ')
            nova_data = input('Nova data (AAAA-MM-DD) (deixe-a em branco para mantê-la inalterada): ')
            novo_saldo = input('Novo saldo (deixe-o em branco para mantê-lo inalterado): ')

            if novo_nome:
                comando_sql = f'UPDATE contas SET nome_conta = "{novo_nome.title()}" WHERE id_conta = {numero_conta}'
                cursor.execute(comando_sql)
            if nova_data:
                comando_sql = f'UPDATE contas SET data_criacao = "{nova_data}" WHERE id_conta = {numero_conta}'
                cursor.execute(comando_sql)
            if novo_saldo:
                comando_sql = f'UPDATE contas SET saldo_conta = "{novo_saldo}" WHERE id_conta = {numero_conta}'
                cursor.execute(comando_sql)
            
            conexao.commit()
                
            print(f'Conta de número {numero_conta} foi editada com sucesso.')


        if comando == 2:
            numero_conta = int(input('Número da conta: '))

            comando_sql = f'DELETE FROM contas WHERE id_conta = {numero_conta}'

            cursor.execute(comando_sql)
            conexao.commit()

            print(f'Usuário excluído com sucesso.')
            
            
        if comando == 3:
            comando_sql = f'SELECT * FROM contas'
            cursor.execute(comando_sql)
            resultado = cursor.fetchall()
            print(resultado)
    
        if comando == 4:
            cursor.close()
            conexao.close()
            break
    
    elif comando == 3:
        cursor.close()
        conexao.close()
        break