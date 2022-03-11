cpf_list_test = ['080.630.946-25', '875.874.946-12', '215.630.968-21', '147.630.946-25',
                 '196.630.462-12', '080.630.946-25', '162.458.963-36', '789.951.968-62']


def cpf_format_validator(cpf_list):
    cpf_list_format_error_list_test = []
    cpf_list_char_error_list_test = []

    for cpf in cpf_list:
        only_number_cpf = cpf[:3] + cpf[4:7] + cpf[8:11] + cpf[12:15]
        if cpf != '{}.{}.{}-{}'.format(cpf[:3], cpf[4:7], cpf[8:11], cpf[12:15]) or len(only_number_cpf) != 11:
            cpf_list_format_error_list_test.append([cpf_list.index(cpf), cpf])

        try:
            int(only_number_cpf)
        except ValueError:
            cpf_list_char_error_list_test.append([cpf.index(cpf), cpf])

    return cpf_list_format_error_list_test, cpf_list_char_error_list_test


def test_cpf_format_validator():
    assert cpf_format_validator(cpf_list_test) == ([], [])

