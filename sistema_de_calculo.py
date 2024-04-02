def fun_calculo(*args):
    somatorio = {'total_val': 0, 'total_in': 0}
    for valor in args:
        somatorio['total_val'] += valor
        somatorio['total_in'] += 1
    #somatorio['total_in'] = len(args)
    return somatorio

valores = []
resp = ' '
while resp not in 'N':
    try:
        valor = input('Digite um valor inteiro: ').strip()
        
        if valor.isdigit(): # se for um número
            valores.append(int(valor))
        else:
            print('Valor invalido!')
            continue
        continua = True
        while continua:
            resp = input('Digite [S] continua [N] para: ').strip().upper()
            continua = False if resp in 'SN' else True # se 'resp' for S ou N, saia do loop

    except:
        print(f'Erro na hora de converter o valor \nTente mais uma vez')
        break

#valores = tuple(valores)
calculo_tot = fun_calculo(*(tuple(valores))) #transformo em tupla e depois desempacoto
print('-' * 20)
print(f'Total números digitados: {calculo_tot['total_in']}. \nTotal do calculo: {calculo_tot['total_val']}.')