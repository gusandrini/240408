'''
Escreva um programa em python que receba como entrada o crédito
de um cliente e depois o preço de intens comprados por este
cliente. O programa deverá para de solicitar novos preços
quando o crédito disponível foi insuficiente para pagar um dos
intens. Ao final, exiba o crédto restante.

'''

credito = float(input('Crédito: '))

quero_comprar = input ('Gostaria de comprar?')
while quero_comprar.lower() == 's' or 'sim':

    while credito > 0: 
        item = float(input('Preço do item: R$'))

        while item < 0:
            print('Valor negativo!')
            item = float(input('Preço do item: R$ '))
        print(f'Crédito restante: R$ {(credito-item): .2f}')
        quero_comprar = input ('Gostaria de continuar comprando?')
        
        if item > credito:
            print('Compra negada! Saldo insuficiente.')
            print(f'Saldo: R$ {credito: .2f}')
            continue
            #break
        credito-=item

        while quero_comprar.lower() == 'n' or 'nao' or 'não':
            print('Obrigado,volte sempre!')
            break


#while credito > 0:
 #           quero_comprar.lower() == 'n' or 'nao' or 'não'
 #           print('Obrigado, volte sempre!')
#            break
 #   print(f'Crédito restante: R$ {credito: .2f}')
 #   quero_comprar = input ('Gostaria de comprar?')