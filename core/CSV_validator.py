from utils.decode_strings import normalMap

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


class CsvinpersistenceFilter:
    lista = []

    def __init__(self, readed_csv=csv[1:]):
        self.readed_csv = readed_csv

    def name_filter(self, file):
        self.lista = []
        for x, y in enumerate(file):
            if len(y[0]) > 25:
                self.lista.append([x + 2, y[0]])
        name_errors = ['names longger than 25 char', self.lista]
        print(name_errors)

    def email_filter(self, file):
        # todo: refazer o nome dessas variaveis ( kaique )
        self.lista = []
        # remove acentos
        names = [x[0].translate(normalize) for x in file]
        formated_names = [x.split(' ') for x in names]
        emails = [y[1][0] for x, y in enumerate(file)]
        emails_names = [x.split('@')[0] for x in emails]

        first_and_last_name_from_names = [f'{x[0].lower()} {x[-1].lower()}' for x in formated_names]
        first_and_last_name_from_email = [x.replace('.', ' ') for x in emails_names]

        difference = list(set(first_and_last_name_from_names) - set(first_and_last_name_from_email))

        print(names)
        print(formated_names)
        print(emails_names)
        print(first_and_last_name_from_names)
        print(first_and_last_name_from_email)
        print(first_and_last_name_from_names == first_and_last_name_from_email)

    # TODO: aqui vc vai criar o filtro de idade de acordo com o codigo, percorrendo o arquivo
    def age_filter(self, file):
        pass

    # TODO: aqui vc vai criar o filtro de telefone de acordo com o codigo, percorrendo o arquivo
    def phone_filter(self, file):
        pass


c = CsvinpersistenceFilter()
# c.name_filter(c.readed_csv)
c.email_filter(c.readed_csv)
