class CsvInconsistencyFilter:
    """
    Essa Classe é responsável por organizar as funções estáticas
    de filtragem de por lista que forem passadas nas funções.
    :param:
    os parametros sao padrões:
    uma lista do que deve ser verificado
    uma lista de erro de formato
    uma lista de erro de caractere
    """

    @staticmethod
    def name_format_inconsistency_filter(name_list, error_list):
        """
        essa funcao verifica o tamanho dos elementos e adiciona na lista os que nao passarem no filtro
        :param name_list: lista de nomes
        :param error_list: lista de erros com o indice que nao passarem no filtro
        :return: sem retorno apenas printa para o terminal/user o indice e o erro
        """
        for x in name_list:
            if len(x) > 25:
                error_list.append([name_list.index(x) + 2, x])

        if len(error_list) > 0:
            print()
            print('*' * 35)
            print("|     ERRO     de    tamanho      |")
            print('*' * 35)
            print("Tamanho maximo petmitido: 25 char |")
            print('*' * 35)
            print("linha com erro |  nomes com erro  |")
            for error in error_list:
                print(error)
            print('-' * 35)
            print()
        else:
            print()
            print('-' * 50)
            print("Nenhum Erro de tamanho encontrado nos NOMES.")
            print('-' * 50)
            print()

    @staticmethod
    def name_char_inconsistency_filter(name_list, error_list):
        """
        essa funcao verifica o se a lista passada existe algum numero
        :param name_list: lista de nomes
        :param error_list: lista de erros com o indice que nao passarem no filtro
        :return: sem retorno apenas printa para o terminal/user o indice e o erro
        """
        for name in name_list:
            for char in name:
                if char.isdigit():
                    error_list.append([name_list.index(name) + 2, char])

        if len(error_list) > 0:
            print()
            print('*' * 35)
            print("|      ERRO     de    caracteres    |")
            print('*' * 35)
            print("linha com erro | caracteres errados |")
            for x in error_list:
                print(f'      {x[0]}                 "{x[1]}"')
            print('-' * 35)
            print()
        else:
            print()
            print('-' * 50)
            print("Nenhum Erro de caracetere encontrado nos NOMES.")
            print('-' * 50)
            print()

    @staticmethod
    def email_format_inconsistency_filter(names, email_list, error_list):
        """
        Essa função confere se os emails estão no padrão do teste primeiro.ultimo nome
        :param names: lista de nomes para conferir se bate o primeiro.ultimo nome
        :param email_list: lista de emails para serem filtrados
        :param error_list: lista de erros que será usada para o append
        :return: sem retorno apenas printa para o terminal/user o indice + padrao requerido
        """

        formatted_names = [name.split(' ') for name in names]
        email_names = [email.split('@')[0] for email in email_list]
        first_and_last_name_from_names = [f'{name[0].lower()} {name[-1].lower()}' for name in formatted_names]
        first_and_last_name_from_email = [name.replace('.', ' ') for name in email_names]

        difference = list(set(first_and_last_name_from_names) - set(first_and_last_name_from_email))
        if len(difference) > 0:
            for name in difference:
                error_list.append([first_and_last_name_from_names.index(name) + 2, name.replace(' ', '.')])

        error_list.sort()
        if len(error_list) > 0:
            print()
            print('*' * 35)
            print("|  ERRO   de formatação de emails |")
            print('*' * 35)
            print("linha com erro |  formato correto |")
            for x in error_list:
                print(f'      {x[0]}           nome.ultomo_nome|')
            print('-' * 35)
            print()
        else:
            print()
            print('-' * 50)
            print("Nenhum Erro de formatação encontrado nos EMAILS.")
            print('-' * 50)
            print()

    @staticmethod
    def age_format_inconsistency_filter(format_error_list, age_list):
        """
        Essa função filtra se as idades não são do tipo inteiro
        :param format_error_list: lista que vai ser usada para o append dos indices + erros
        :param age_list: lista de numeros inteiros
        :return: apenas printa para o usuario a lista com os indices + erros
        """
        for age in age_list:
            try:
                int(age)
            except ValueError:
                format_error_list.append([age_list.index(age) + 2, age])

        if len(format_error_list) > 0:
            format_error_list.sort()
            print()
            print('*' * 35)
            print("|  ERRO   de formatação de idades |")
            print('*' * 35)
            print("A idade deve ser um numero inteiro| ")
            print('*' * 35)
            print("linha com erro |  caractere errado|")
            for x in format_error_list:
                print(f'  {x[0]}                     {x[1]}')
            print('-' * 35)
            print()
        else:
            print()
            print('-' * 50)
            print("Nenhum Erro de formatação encontrado nas IDADES.")
            print('-' * 50)
            print()

    @staticmethod
    def phone_format_inconsistency_filter(phone_list, format_error_list, character_error_list):
        """
        Essa função filtra os numeros que estão fora do padrão do formato requerido no teste
        :param phone_list: lista de numeros telefonicos no formato '(xx) xxxx-xxxxx'
        :param format_error_list: lista que será usada para o erro de formatos
        :param character_error_list: lista que será usada para o erro de caracteres
        :return: apenas printa para o usuario a lista com os indices + erros
        """
        for phone in phone_list:
            only_numbers_phone = phone[1:3] + phone[5:9] + phone[10:16]
            if phone != '({}) {}-{}'.format(phone[1:3], phone[5:9], phone[10:16]) or len(only_numbers_phone) != 11:
                format_error_list.append([phone_list.index(phone) + 2, phone])

                for number in only_numbers_phone:
                    if not number.isdigit():
                        character_error_list.append(
                            [phone_list.index(phone), phone]
                        )

        if len(format_error_list) > 0:
            print()
            print('*' * 35)
            print("| ERRO de formatação de telefones |")
            print('*' * 35)
            print(" telefones serão aceitos somente  |")
            print(" no formato: (DDD) xxxx-xxxxx     |")
            print('*' * 35)
            print("linha com erro | telefones errados|")
            for x in format_error_list:
                print(f'   {x[0]}             {x[1]}')
            print('-' * 35)
            print()
        else:
            print()
            print('-' * 50)
            print("Nenhum Erro de formatação encontrado nos TELEFONES.")
            print('-' * 50)
            print()
        if len(character_error_list) > 0:
            print()
            print('*' * 35)
            print("| ERRO de  caracteres  indevidos  |")
            print('*' * 35)
            print(" Apenas números serão aceitos e   |")
            print(" no formato: (DDD) xxxx-xxxxx     |")
            print('*' * 35)
            print("linha com erro | telefones errados|")
            for x in format_error_list:
                print(f'   {x[0]}             {x[1]}')
            print('-' * 35)
            print()
        else:
            print()
            print('-' * 50)
            print("Nenhum Erro de Caractere encontrado nos TELEFONES.")
            print('-' * 50)
            print()

    @staticmethod
    def cpf_format_inconsistency_filter(cpf_list, format_error_list, character_error_list):
        """
        Essa função filtra os cpfs para o formato requerido no teste
        :param cpf_list: lista de cpfs no formato 'xxx.xxx.xxx-xx'
        :param format_error_list: lista que será usada para o erro de formatos
        :param character_error_list: lista que será usada para o erro de caracteres
        :return: apenas printa para o usuario a lista com os indices + erros
        """
        for cpf in cpf_list:
            only_number_cpf = cpf[:3] + cpf[4:7] + cpf[8:11] + cpf[12:15]
            if cpf != '{}.{}.{}-{}'.format(cpf[:3], cpf[4:7], cpf[8:11], cpf[12:15]) or len(only_number_cpf) != 11:
                format_error_list.append([cpf_list.index(cpf) + 2, cpf])

            try:
                int(only_number_cpf)
            except ValueError:
                character_error_list.append([cpf_list.index(cpf) + 2, cpf])

        if len(format_error_list) > 0:
            print()
            print('*' * 35)
            print("| ERRO  de  formatação nos CPFs   |")
            print('*' * 35)
            print(" Apenas números serão aceitos e   |")
            print(" no formato:   xxx.xxx.xxx-xx     |")
            print('*' * 35)
            print("linha com erro |  CPFS  com erro  |")
            for x in format_error_list:
                print(f'   {x[0]}              {x[1]}')
            print('-' * 35)
            print()
        else:
            print()
            print('-' * 50)
            print("Nenhum Erro de formatação encontrado nos CPFs.")
            print('-' * 50)
            print()
        if len(character_error_list) > 0:
            print()
            print('*' * 35)
            print("| ERRO  de  caractere  nos CPFs   |")
            print('*' * 35)
            print(" Apenas números serão aceitos e   |")
            print(" no formato:   xxx.xxx.xxx-xx     |")
            print('*' * 35)
            print("linha com erro |  CPFS  com erro  |")
            for x in character_error_list:
                print(f'   {x[0]}        {x[1]}')
            print('-' * 35)
            print()
        else:
            print()
            print('-' * 50)
            print("Nenhum Erro de caractere encontrado nos CPFs.")
            print('-' * 50)
            print()

    @staticmethod
    def birth_date_inconsistency_filter(data_nascimento_list, format_error_list, character_error_list):
        """
        Essa função filtra datas para o padrão requerido no teste
        :param data_nascimento_list: lista de datas no formato 'xx/xx/xx'
        :param format_error_list: lista que será usada para o erro de formatos
        :param character_error_list: lista que será usada para o erro de caracteres
        :return: apenas printa para o usuario a lista com os indices + erros
        """
        for data in data_nascimento_list:
            only_number_data = data[:2] + data[3:5] + data[6:10]

            if data != '{}/{}/{}'.format(data[:2], data[3:5], data[6:10]) or len(only_number_data) != 8:
                format_error_list.append([data_nascimento_list.index(data) + 2, data])

            try:
                int(only_number_data)
            except ValueError:
                character_error_list.append([data_nascimento_list.index(data) + 2, data])

        if len(format_error_list) > 0:
            print()
            print('*' * 35)
            print("      ERRO de formatação          |")
            print("      nas datas de nascimento")
            print('*' * 35)
            print("    Utilize o formato xx/xx/xx    |")
            print('*' * 35)
            print("linha com erro |  datas  com erro  |")
            for x in format_error_list:
                print(f'   {x[0]}               {x[1]}     |')
            print('-' * 35)
            print()
        else:
            print()
            print('-' * 50)
            print("Nenhum Erro de formtação nas DATAS DE NASCIMENTO.")
            print('-' * 50)
            print()
        if len(character_error_list) > 0:
            print()
            print('*' * 35)
            print("      ERRO de caractere            |")
            print("      nas datas de nascimento")
            print('*' * 35)
            print("Utilize apenas numeros no formato  |")
            print("  xx/xx/xx (onde x são os números) |")
            print('*' * 35)
            print("linha com erro |  datas  com erro  |")
            for x in character_error_list:
                print(f'   {x[0]}               {x[1]}      |')
            print('-' * 35)
            print()
        else:
            print()
            print('-' * 50)
            print("Nenhum Erro de formtação nas DATAS DE NASCIMENTO.")
            print('-' * 50)
            print()

    @staticmethod
    def register_date_inconsistency_filter(data_cadastro_list, format_error_list, character_error_list):
        """
        Essa função filtra datas para o padrão requerido no teste
        :param data_cadastro_list: lista de datas no formato 'xx/xx/xx'
        :param format_error_list: lista que será usada para o erro de formatos
        :param character_error_list: lista que será usada para o erro de caracteres
        :return: apenas printa para o usuario a lista com os indices + erros
        """
        for data in data_cadastro_list:
            only_number_data = data[:2] + data[3:5] + data[6:10]
            if data != '{}/{}/{}'.format(data[:2], data[3:5], data[6:10]) or len(only_number_data) != 8:
                format_error_list.append([data_cadastro_list.index(data) + 2, data])

            try:
                int(only_number_data)
            except ValueError:
                character_error_list.append([data_cadastro_list.index(data) + 2, data])

        if len(format_error_list) > 0:
            print()
            print('*' * 35)
            print("      ERRO de formatação          |")
            print("      nas DATAS DE CADASTRO       |")
            print('*' * 35)
            print("    Utilize o formato xx/xx/xx    |")
            print('*' * 35)
            print("linha com erro |  datas  com erro  |")
            for x in format_error_list:
                print(f'   {x[0]}               {x[1]}     |')
            print('-' * 35)
            print()
        else:
            print()
            print('-' * 50)
            print("Nenhum Erro de formtação nas DATAS DE CADASTRO.")
            print('-' * 50)
            print()
        if len(character_error_list) > 0:
            print()
            print('*' * 35)
            print("      ERRO de caractere            |")
            print("      nas DATAS DE CADASTRO")
            print('*' * 35)
            print("Utilize apenas numeros no formato  |")
            print("  xx/xx/xx (onde x são os números) |")
            print('*' * 35)
            print("linha com erro |  datas  com erro  |")
            for x in character_error_list:
                print(f'   {x[0]}               {x[1]}      |')
            print('-' * 35)
            print()
        else:
            print()
            print('-' * 50)
            print("Nenhum Erro de formtação nas DATAS DE CADASTRO.")
            print('-' * 50)
            print()
