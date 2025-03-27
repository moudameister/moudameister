#Gerenciador de pagamentos.
print('=====CABORÉMART=====')
valor = float(input('Digite o valor da compra: R$ '))
vista = valor - valor * 0.1
cartao = valor - valor * 0.05
print('Qual será a forma de pagamento?')
print('[1] Á VISTA/CHEQUE')
print('[2] Á VISTA CARTÃO')
print('[3] 2x NO CARTÃO')
print('[4] 3x OU MAIS NO CARTÃO')
esc = str(input('Sua escolha: '))
if esc=='1':
    print(f'Como você comprou á vista, sua compra de R${valor} ficou por R${vista}')
elif esc=='2':
    print(f'Como você pagou à vista no cartão, sua compra de R${valor} ficou por R${cartao}')
elif esc=='3':
    par2 = valor / 2
    print(f'Parcelando em 2x no catrão, sua compra de R${valor} fica por 2 de R${par2} ')
elif esc=='4':
    parceladas = int(input('Em quantas vezes deseja parcelar sua compra: '))
    par3 = valor * 1.20 / parceladas
    print(f'Parcelando sua compra de R${valor} em {parceladas}, o valor fica por {parceladas} de R${par3}')
    print(f'Sua compra de R${valor} vai custar R${valor * 1.20} no final.')
