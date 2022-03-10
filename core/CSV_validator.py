from utils.decode_strings import normalMap
from utils.cpf_validator import cpf_validator

normalize = str.maketrans(normalMap)


class CsvReader:
    def __init__(self, csv_file_path: str) -> None:
        self.csv_file = csv_file_path

    def reader(self):
        with open(
                self.csv_file,
                'r',
                encoding='utf-8',
                errors='ignore',
        ) as file:
            results = []
            for line in file:
                words = line.strip().split(',')
                results.append([words[0], words[1:]])
        return results


c = CsvReader('/home/kaiquecosta/kaique/projetos pessoais/ryan_test/cadastros.csv')
csv = c.reader()


class CsvRestictionsErrors:
    @staticmethod
    def name_format_validator(name_list, error_list):
        for x in name_list:
            if len(x) > 25:
                error_list.append([name_list.index(x) + 2, x])

        if len(error_list) > 0:
            print("Max field Charactere")
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
        print("Error:")
        print('(O formato do email deve ser primeiro.ultimo nome)')
        print("linha | formato errado")
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
                format_error_list.append([phone_list.index(phone), phone])

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

            for number in only_number_cpf:
                if not number.isdigit():
                    character_error_list.append(
                        [cpf_list.index(cpf) + 2, cpf]
                    )

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


class CsvinpersistenceFilter(CsvRestictionsErrors):
    format_error_list = []
    character_error_list = []

    def __init__(self, readed_csv=None):
        if readed_csv is None:
            readed_csv = csv[1:]
        self.readed_csv = readed_csv

    def name_filter(self, file):
        self.format_error_list = []
        self.character_error_list = []
        names = [y[0] for x, y in enumerate(file)]

        self.name_format_validator(names, self.format_error_list)
        self.name_char_validator(names, self.character_error_list)

    def email_filter(self, file):
        # todo: refazer o nome dessas variaveis ( kaique )
        self.format_error_list = []
        # remove acentos
        names = [x[0].translate(normalize) for x in file]
        emails = [y[1][0] for x, y in enumerate(file)]
        self.email_format_validator(names, emails, self.format_error_list)

    def age_filter(self, file):
        self.format_error_list = []
        ages = [y[3] for x, y in file]
        self.age_format_validator(self.format_error_list, ages)

    def phone_filter(self, file):
        self.format_error_list = []
        self.character_error_list = []
        phone_list = [y[2] for x, y in file]

        self.phone_format_validator(phone_list, self.format_error_list, self.character_error_list)

    # todo : faz telefone e as datas como está aqui ok?
    def cpf_filter(self, file):
        self.format_error_list = []
        self.character_error_list = []
        cpf_list = [y[1] for x, y in file]

        self.cpf_format_validator(cpf_list, self.format_error_list, self.character_error_list)

    def data_cadastro_filter(self, file):
        self.format_error_list = []
        data_d_list = [y[5] for x, y in file]

        for data in data_d_list:
            if data != '{}/{}/{}'.format(data[:2], data[3:5], data[6:10]):
                self.format_error_list.append([data_d_list.index(data), data])

        if len(self.format_error_list) > 0:
            print("Erro de formato:")
            print("O formato deve ser : 'xx/xx/xxxx'")
            print("[row | value]")
            for x in self.format_error_list:
                print(x)
            print()

    # TODO validar
    def data_nascimento_filter(self, file):
        self.format_error_list = []
        data_n_list = [y[4] for x, y in file]

        for data in data_n_list:
            if data != '{}/{}/{}'.format(data[:2], data[3:5], data[6:10]):
                self.format_error_list.append([data_n_list.index(data) + 2, data])
                print(data[:2] + data[3:5] + data[6:10])
        if len(self.format_error_list) > 0:
            print("Erro de formato:")
            print("O formato deve ser : 'xx/xx/xxxx'")
            print("[row | value]")
            for x in self.format_error_list:
                print(x)
            print()


c = CsvinpersistenceFilter()
# c.name_filter(c.readed_csv)
# c.age_filter(c.readed_csv)
# c.email_filter(c.readed_csv)
c.cpf_filter(c.readed_csv)
# c.phone_filter(c.readed_csv)
# c.data_cadastro_filter(c.readed_csv)
# c.data_nascimento_filter(c.readed_csv)
# # c.name_filter(c.readed_csv)
# print(c.readed_csv)
# c.email_filter(c.readed_csv)
