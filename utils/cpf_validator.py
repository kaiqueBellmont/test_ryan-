cpf = '08063094662'
lista = ['08063094662', '12345678912']


# Validar se o documento original é igual o gerado.
# validar se todos os numeros sao iguals.

def cpf_validator(original_document: str, *args):
    document_digits = original_document[:9]
    formula_number = 10
    digit1 = 0
    for x in range(len(document_digits)):
        # print(int(document[x]) * number)
        digit1 += int(document_digits[x]) * formula_number
        formula_number -= 1
    # caso for maior do que 10, digito tem que ser 0
    digit1 = digit1 % 11
    if digit1 > 10:
        digit1 = 0
    else:
        digit1 = 11 - digit1

    document_digits = document_digits + str(digit1)
    formula_number = 11
    digit2 = 0

    for x in range(len(document_digits)):
        digit2 += int(document_digits[x]) * formula_number
        formula_number -= 1
    digit2 = digit2 % 11
    if digit2 > 10:
        digit2 = 0
    else:
        digit2 = 11 - digit2

    document_digits = document_digits + str(digit2)
    print(document_digits)

