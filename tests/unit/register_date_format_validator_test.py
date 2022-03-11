register_date_test_list = ['10/05/1996', '17/05/1998', '18/05/2001', '17/08/2022', '28/06/1994', '11/05/1996',
                           '30/05/1999', '31/03/2003', '16/10/2021', '10/06/2007', '10/11/2020', '24/11/2019']


def register_date_format_validator(register_date_list):
    register_date_format_error_list_test = []
    register_date_char_error_list_test = []
    for data in register_date_list:
        only_number_data = data[:2] + data[3:5] + data[6:10]
        if data != '{}/{}/{}'.format(data[:2], data[3:5], data[6:10]) or len(only_number_data) != 8:
            register_date_format_error_list_test.append([register_date_list.index(data) + data])

        try:
            int(only_number_data)
        except ValueError:
            register_date_char_error_list_test.append([register_date_list.index(data), data])

    return register_date_format_error_list_test, register_date_char_error_list_test


def test_register_date_format_validator():
    assert register_date_format_validator(register_date_test_list) == ([], [])
