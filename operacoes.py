operacao_invalida = None 
primeiro_numero = None 
segundo_numero = None 
tipo_operacao = None 
resultado = None 

def text_prompt(msg):
    try: 
        return raw_input(msg)
    except NameError: return input(msg)
    
    
operacao_invalida = False
primeiro_numero = float(text_prompt('Qual o primeiro número: '))
segundo_numero = float(text_prompt('Qual o segundo número: '))
tipo_operacao = text_prompt('Qual a operação desejada?').lower()
if tipo_operacao == 'soma' or tipo_operacao == 'so' or tipo_operacao == '+':
    resultado = primeiro_numero + segundo_numero
    tipo_operacao = 'soma' 
elif tipo_operacao == 'subtração' or tipo_operacao == 'su' or tipo_operacao == '-': 
    resultado = primeiro_numero - segundo_numero 
    tipo_operacao = 'subtração'
elif tipo_operacao == 'multiplicação' or tipo_operacao == 'mu' or tipo_operacao == 'x': 
    resultado = primeiro_numero * segundo_numero
    tipo_operacao = 'multiplicação' 
elif tipo_operacao == 'divisão' or tipo_operacao == 'di' or tipo_operacao == '/': 
    resultado = primeiro_numero / segundo_numero 
    tipo_operacao = 'divisão' 
else:
    resultado = 'Não é possível realizar a operação!' 
    operacao_invalida = True 
if operacao_invalida:
    print(resultado)
else: 
    print(''.join([str(x) for x in ['0 resultado da ', tipo_operacao.title(),' dos números é: ', (resultado)]]))