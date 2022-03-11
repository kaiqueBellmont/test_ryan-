from csv_reader import CsvReader
from csv_persistence_filter import CsvinpersistenceFilter


def main():
    reader = CsvReader('cadastros.csv')
    csv = reader.reader()
    cursor = CsvinpersistenceFilter(csv)
    cursor.name_filter(cursor.readed_csv)
    cursor.email_filter(cursor.readed_csv)
    cursor.cpf_filter(cursor.readed_csv)
    cursor.phone_filter(cursor.readed_csv)
    cursor.data_nascimento_filter(cursor.readed_csv)
    cursor.data_cadastro_filter(cursor.readed_csv)


main()
