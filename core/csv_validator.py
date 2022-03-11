from utils.decode_strings import normalMap

normalize = str.maketrans(normalMap)


class CsvValidator:
    @staticmethod
    def name_format_validator(name_list, error_list):
        for x in name_list:
            if len(x) > 25:
                error_list.append([name_list.index(x) + 2, x])

        if len(error_list) > 0:
            print("Max field length exceded (25)")
            print("Erro de formato:")
            print("linha | caractere")
            for x in error_list:
                print(x)
            print()

    @staticmethod
    def name_char_validator(name_list, error_list):
        for x in name_list:
            for y in x:
                if y.isdigit():
                    error_list.append([name_list.index(x) + 2, y])

        if len(error_list) > 0:
            print("Erro de caracteres:")
            print("linha | caractere")
            for x in error_list:
                print(x)
            print()

    @staticmethod
    def email_format_validator(names, email_list, error_list):

        formated_names = [x.split(' ') for x in names]
        emails_names = [x.split('@')[0] for x in email_list]
        first_and_last_name_from_names = [f'{x[0].lower()} {x[-1].lower()}' for x in formated_names]
        first_and_last_name_from_email = [x.replace('.', ' ') for x in emails_names]

        difference = list(set(first_and_last_name_from_names) - set(first_and_last_name_from_email))
        if len(difference) > 0:
            for x in difference:
                error_list.append([first_and_last_name_from_names.index(x) + 2, x.replace(' ', '.')])

        error_list.sort()
        if len(error_list) > 0:
            print("Error:")
            print('(O formato do email deve ser primeiro.ultimo nome)')
            print("linha | formato correto:")
            for x in error_list:
                print(f'  {x[0]}     {x[1]}')

    @staticmethod
    def age_format_validator(format_error_list, age_list):
        for x in age_list:
            try:
                int(x)
            except ValueError:
                format_error_list.append([age_list.index(x) + 2, x])

        if len(format_error_list) > 0:
            format_error_list.sort()
            print("Erro:")
            print("(O campo idade deve ser um número inteiro)")
            print("linha | caracteres")
            for x in format_error_list:
                print(f'  {x[0]}         {x[1]}')
            print()

    @staticmethod
    def phone_format_validator(phone_list, format_error_list, character_error_list):
        for phone in phone_list:
            only_numbers_phone = phone[1:3] + phone[5:9] + phone[10:16]
            if phone != '({}) {}-{}'.format(phone[1:3], phone[5:9], phone[10:16]) or len(only_numbers_phone) != 11:
                format_error_list.append([phone_list.index(phone) +2, phone])

                for number in only_numbers_phone:
                    if not number.isdigit():
                        character_error_list.append(
                            [phone_list.index(phone), phone]
                        )

        if len(format_error_list) > 0:
            print("Erro de formato:")
            print("O formato deve ser : '(xx) xxxx-xxxxx'")
            print("  row   |   value")
            for x in format_error_list:
                print(f'   {x[0]}        {x[1]}')
            print()
        else:
            print("Telefones sem erro de formato")
        if len(character_error_list) > 0:
            print("Erro de character:")
            print("O campo permite apenas penas DDD + Numero")
            print("  row   |   value")
            for x in format_error_list:
                print(f'   {x[0]}        {x[1]}')
            print()
        else:
            print("Telefones sem erro de char")

    @staticmethod
    def cpf_format_validator(cpf_list, format_error_list, character_error_list):
        for cpf in cpf_list:
            only_number_cpf = cpf[:3] + cpf[4:7] + cpf[8:11] + cpf[12:15]
            if cpf != '{}.{}.{}-{}'.format(cpf[:3], cpf[4:7], cpf[8:11], cpf[12:15]) or len(only_number_cpf) != 11:
                format_error_list.append([cpf_list.index(cpf) + 2, cpf])

            try:
                int(only_number_cpf)
            except ValueError:
                character_error_list.append([cpf.index(cpf) + 2, cpf])

        if len(format_error_list) > 0:
            print("Erro de formato:")
            print("O formato deve ser : 'xxx.xxx.xxx-xx'")
            print("  row   |   value")
            for x in format_error_list:
                print(f'   {x[0]}        {x[1]}')
            print()
        else:
            print("CPFs sem erro de formato")
        if len(character_error_list) > 0:
            print("Erro de character:")
            print("O campo permite apenas numeros no formato xxx.xxx.xxx-xx'")
            print("  row   |   value")
            for x in character_error_list:
                print(f'   {x[0]}        {x[1]}')
            print()
        else:
            print("CPFs sem erro de char")

    @staticmethod
    def data_nascimento_validator(data_nascimento_list, format_error_list, character_error_list):
        for data in data_nascimento_list:
            only_number_data = data[:2] + data[3:5] + data[6:10]
            if data != '{}/{}/{}'.format(data[:2], data[3:5], data[6:10]) or len(only_number_data) != 8:
                format_error_list.append([data_nascimento_list.index(data) + 2, data])

            try:
                int(only_number_data)
            except ValueError:
                character_error_list.append([data_nascimento_list.index(data) + 2, data])

        if len(format_error_list) > 0:
            print("Erro de formato:")
            print("O formato deve ser : 'xx/xx/xxxx'")
            print("  row   |   value")
            for x in format_error_list:
                print(f'   {x[0]}        {x[1]}')
            print()
        else:
            print("DATA NASCIMENTO sem erro de formato")
        if len(character_error_list) > 0:
            print("Erro de character:")
            print("O campo permite apenas numeros no formato xx/xx/xxxx'")
            print("  row   |   value")
            for x in character_error_list:
                print(f'   {x[0]}        {x[1]}')
            print()
        else:
            print("DATA NASCIMENTO sem erro de char")

    @staticmethod
    def data_cadastro_validator(data_cadastro_list, format_error_list, character_error_list):
        for data in data_cadastro_list:
            only_number_data = data[:2] + data[3:5] + data[6:10]
            if data != '{}/{}/{}'.format(data[:2], data[3:5], data[6:10]) or len(only_number_data) != 8:
                format_error_list.append([data_cadastro_list.index(data) + 2, data])

            try:
                int(only_number_data)
            except ValueError:
                character_error_list.append([data_cadastro_list.index(data) + 2, data])

        if len(format_error_list) > 0:
            print("Erro de formato:")
            print("O formato deve ser : 'xx/xx/xxxx'")
            print("  row   |   value")
            for x in format_error_list:
                print(f'   {x[0]}        {x[1]}')
            print()
        else:
            print("DATA CADATRO sem erro de formato")
        if len(character_error_list) > 0:
            print("Erro de character:")
            print("O campo permite apenas numeros no formato xx/xx/xxxx'")
            print("  row   |   value")
            for x in character_error_list:
                print(f'   {x[0]}        {x[1]}')
            print()
        else:
            print("DATA CADASTRO sem erro de char")

# c = CsvinpersistenceFilter()
# # c.name_filter(c.readed_csv)
# # c.age_filter(c.readed_csv)
# # c.email_filter(c.readed_csv)
# # c.cpf_filter(c.readed_csv)
# # c.phone_filter(c.readed_csv)
# c.data_cadastro_filter(c.readed_csv)
# # c.data_nascimento_filter(c.readed_csv)
# # # c.name_filter(c.readed_csv)
# # print(c.readed_csv)
# # c.email_filter(c.readed_csv)
