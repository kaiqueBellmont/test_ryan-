# não usei path ou algo do tipo, pois precisaria do os.system, e no teste, nao podia importar...
from csv_reader import CsvReader
from csv_inconsistency_checker import CsvInconsistencyChecker


def main():
    print()
    arquivo = input("Digite o path absoluto do seu arquivo .csv: (ou somente copie e cole ele aqui)")
    arquivo = arquivo if arquivo else 'cadastros.csv'
    reader = CsvReader(arquivo)
    csv = reader.reader()

    # instancia um objeto da classe CsvInconsistencyChecker apenas para chamar as funções
    cursor = CsvInconsistencyChecker()

    # toda vez que for chamar uma função da classe, passa o arquivo que a classe CsvReader já leu.
    cursor.name_inconsistency_checker(csv)
    cursor.email_inconsistency_checker(csv)
    cursor.age_inconsistency_checker(csv)
    cursor.cpf_inconsistency_checker(csv)
    cursor.phone_inconsistency_checker(csv)
    cursor.birth_date_inconsistency_checker(csv)
    cursor.register_date_inconsistency_checker(csv)


if __name__ == '__main__':
    main()
