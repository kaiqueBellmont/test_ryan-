# local files
from csv_inconsistency_filter import CsvInconsistencyFilter
from utils import normalMap

# variable receives an accent normalize function, used to normalize csv file data and compare names
normalize = str.maketrans(normalMap)


class CsvInconsistencyChecker(CsvInconsistencyFilter):
    """
    Essa classe foi utilizada para armazenar as funções que lêem o arquivo CSV, extrai o que precisa,
    e passa para os filtros, armazenados na outra classe.
    como uma espécie de controllers...
    """
    # listas utilizadas para armazenar erros do teste
    format_error_list = []
    character_error_list = []

    # esse init é utilizado para a a utilização do arquivo aberto da classe 'CsvReader'
    # ele inicia uma instancia do arquivo aberto para a utilização da classe

    def name_inconsistency_checker(self, file):
        """
        Essa função recebe um arquivo CSV já aberto, utiliza listas da classe como instancia,
        extrai os campos do csv que vai utilizar, e chama as funções que filtram e printam os erros
        :param file: csv já aberto
        :return: não retorna nada,
        """
        self.format_error_list = []
        self.character_error_list = []
        names = [y[0] for x, y in enumerate(file)]
        names = names[1:]
        self.name_format_inconsistency_filter(names, self.format_error_list)
        self.name_char_inconsistency_filter(names, self.character_error_list)

    def email_inconsistency_checker(self, file):
        """
        Essa função recebe um arquivo CSV já aberto, utiliza listas da classe como instancia,
        extrai os campos do csv que vai utilizar, e chama as funções que filtram e printam os erros
        :param file: csv já aberto
        :return: não retorna nada,
        """
        self.format_error_list = []
        # remove acentos
        names = [x[0].translate(normalize) for x in file]
        emails = [y[1][0] for x, y in enumerate(file)]

        names = names[1:]
        emails = emails[1:]
        self.email_format_inconsistency_filter(names, emails, self.format_error_list)

    def age_inconsistency_checker(self, file):
        """
        Essa função recebe um arquivo CSV já aberto, utiliza listas da classe como instancia,
        extrai os campos do csv que vai utilizar, e chama as funções que filtram e printam os erros
        :param file: csv já aberto
        :return: não retorna nada,
        """
        self.format_error_list = []
        ages = [y[3] for x, y in file]
        ages = ages[1:]
        self.age_format_inconsistency_filter(self.format_error_list, ages)

    def phone_inconsistency_checker(self, file):
        """
        Essa função recebe um arquivo CSV já aberto, utiliza listas da classe como instancia,
        extrai os campos do csv que vai utilizar, e chama as funções que filtram e printam os erros
        :param file: csv já aberto
        :return: não retorna nada,
        """
        self.format_error_list = []
        self.character_error_list = []
        phone_list = [y[2] for x, y in file]
        phone_list = phone_list[1:]
        self.phone_format_inconsistency_filter(phone_list, self.format_error_list, self.character_error_list)

    def cpf_inconsistency_checker(self, file):
        """
        Essa função recebe um arquivo CSV já aberto, utiliza listas da classe como instancia,
        extrai os campos do csv que vai utilizar, e chama as funções que filtram e printam os erros
        :param file: csv já aberto
        :return: não retorna nada,
        """
        self.format_error_list = []
        self.character_error_list = []
        cpf_list = [y[1] for x, y in file]
        cpf_list = cpf_list[1:]

        self.cpf_format_inconsistency_filter(cpf_list, self.format_error_list, self.character_error_list)

    def register_date_inconsistency_checker(self, file):
        """
        Essa função recebe um arquivo CSV já aberto, utiliza listas da classe como instancia,
        extrai os campos do csv que vai utilizar, e chama as funções que filtram e printam os erros
        :param file: csv já aberto
        :return: não retorna nada,
        """
        self.format_error_list = []
        self.character_error_list = []
        data_d_list = [y[5] for x, y in file]
        data_d_list = data_d_list[1:]
        self.register_date_inconsistency_filter(data_d_list, self.format_error_list, self.character_error_list)

    def birth_date_inconsistency_checker(self, file):
        """
        Essa função recebe um arquivo CSV já aberto, utiliza listas da classe como instancia,
        extrai os campos do csv que vai utilizar, e chama as funções que filtram e printam os erros
        :param file: csv já aberto
        :return: não retorna nada,
        """
        self.format_error_list = []
        self.character_error_list = []
        data_n_list = [y[4] for x, y in file]
        data_n_list = data_n_list[1:]

        self.birth_date_inconsistency_filter(data_n_list, self.format_error_list, self.character_error_list)
