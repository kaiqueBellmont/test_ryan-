age_list_test = ['18', '19', '25', '84', '69', '12', '56', '48']


def age_format_validator(age_list):
    age_list_test_error = []
    for x in age_list:
        try:
            int(x)
        except ValueError:
            age_list_test_error.append([age_list.index(x) + 2, x])
        return age_list_test_error


def test_age_format_validator():
    assert len(age_format_validator(age_list_test)) == 0
