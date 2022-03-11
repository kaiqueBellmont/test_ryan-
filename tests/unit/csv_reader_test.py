file = 'put the absolute path on file csv_reader_test.py'


def reader(csv_file):
    with open(
            csv_file,
            'r',
            encoding='utf-8',
            errors='ignore',
    ) as file:
        results = []
        for line in file:
            words = line.strip().split(',')
            results.append([words[0], words[1:]])
    return results


def test_reader_format():
    assert type(
        reader(
            csv_file=file
        )) == list
