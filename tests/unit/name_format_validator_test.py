name_list_test = ['Levi da Cunha',
                  'Maria Fernanda Silva',
                  'Gabriel Santos',
                  'Mirella da Paz',
                  'Cecilia Oliveira']


def name_length_error_list(name_list: list):
    name_list_test_error = []
    for x in name_list:
        if len(x) > 25:
            name_list_test_error.append([name_list.index(x), x])
    return name_list_test_error


def name_char_error_list(name_list):
    name_list_test_error = []
    for x in name_list:
        if x.isdigit():
            name_list_test_error.append([name_list.index(x), x])
    return name_list_test_error


def test_name_format_error_list():
    assert len(name_length_error_list(name_list_test)) == 0


def test_name_char_error_list():
    assert len(name_char_error_list(name_list_test)) == 0
