from csv_validator import CsvValidator
from utils.decode_strings import normalMap

normalize = str.maketrans(normalMap)


class CsvinpersistenceFilter(CsvValidator):
    format_error_list = []
    character_error_list = []

    def __init__(self, readed_csv=None):
        self.readed_csv = readed_csv

    def name_filter(self, file):
        """

        Essa funcao filtra os nomes, de acordo com os requisitos
        """
        self.format_error_list = []
        self.character_error_list = []
        names = [y[0] for x, y in enumerate(file)]
        names = names[1:]
        self.name_format_validator(names, self.format_error_list)
        self.name_char_validator(names, self.character_error_list)

    def email_filter(self, file):
        """

        Essa funcao filtra os nomes, de acordo com os requisitos
        """
        # todo: refazer o nome dessas variaveis ( kaique )
        self.format_error_list = []
        # remove acentos
        names = [x[0].translate(normalize) for x in file]
        emails = [y[1][0] for x, y in enumerate(file)]

        names = names[1:]
        emails = emails[1:]
        self.email_format_validator(names, emails, self.format_error_list)

    def age_filter(self, file):
        """

        Essa funcao filtra as idades, de acordo com os requisitos
        """
        self.format_error_list = []
        ages = [y[3] for x, y in file]
        self.age_format_validator(self.format_error_list, ages)

    def phone_filter(self, file):
        """

        Essa funcao filtra os telefone, de acordo com os requisitos
        """
        self.format_error_list = []
        self.character_error_list = []
        phone_list = [y[2] for x, y in file]
        phone_list = phone_list[1:]
        self.phone_format_validator(phone_list, self.format_error_list, self.character_error_list)

    # todo : faz telefone e as datas como está aqui ok?
    def cpf_filter(self, file):
        """

        Essa funcao filtra os cpfs, de acordo com os requisitos
        """
        self.format_error_list = []
        self.character_error_list = []
        cpf_list = [y[1] for x, y in file]
        cpf_list = cpf_list[1:]

        self.cpf_format_validator(cpf_list, self.format_error_list, self.character_error_list)

    def data_cadastro_filter(self, file):
        """

        Essa funcao filtra as datas de cadastro, de acordo com os requisitos
        """
        self.format_error_list = []
        self.character_error_list = []
        data_d_list = [y[5] for x, y in file]
        data_d_list = data_d_list[1:]
        self.data_cadastro_validator(data_d_list, self.format_error_list, self.character_error_list)


    # TODO validar
    def data_nascimento_filter(self, file):
        """

        Essa funcao filtra as datas de nascimento, de acordo com os requisitos
        """
        self.format_error_list = []
        self.character_error_list = []
        data_n_list = [y[4] for x, y in file]
        data_n_list = data_n_list[1:]

        self.data_nascimento_validator(data_n_list, self.format_error_list, self.character_error_list)
