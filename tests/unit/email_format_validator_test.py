email_list_test = ['levi.cunha@gmail.com',
                   'maria.silva@gmail.com',
                   'gabriel.santos@gmail.com',
                   'mirella.paz@gmail.com',
                   'cecilia.oliveira@gmail.com']

name_list_test = ['Levi da Cunha',
                  'Maria Fernanda Silva',
                  'Gabriel Santos',
                  'Mirella da Paz',
                  'Cecilia Oliveira']


def email_format_validator(names_list, email_list):
    names_list = names_list
    email_list = email_list
    formated_names = [x.split(' ') for x in names_list]
    emails_names = [x.split('@')[0] for x in email_list]
    first_and_last_name_from_names = [f'{x[0].lower()} {x[-1].lower()}' for x in formated_names]
    first_and_last_name_from_email = [x.replace('.', ' ') for x in emails_names]

    difference = list(set(first_and_last_name_from_names) - set(first_and_last_name_from_email))
    return difference


def test_email_and_names_difference():
    assert len(email_format_validator(names_list=name_list_test, email_list=email_list_test)) == 0
