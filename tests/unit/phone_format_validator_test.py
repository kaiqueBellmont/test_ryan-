phone_numebers_list_test = ['(31) 9913-79563', '(31) 2357-56321', '(31) 4187-87425', '(31) 9913-79563',
                            '(32) 9913-84178', '(62) 9562-79563', '(72) 9913-85849', '(96) 9867-25955', ]


def phone_format_validator(phone_list):
    phone_numebers_list_format_error_list_test = []
    phone_numebers_list_char_error_list_test = []
    for phone in phone_list:
        only_numbers_phone = phone[1:3] + phone[5:9] + phone[10:16]
        if phone != '({}) {}-{}'.format(phone[1:3], phone[5:9], phone[10:16]) or len(only_numbers_phone) != 11:
            phone_numebers_list_format_error_list_test.append([phone_list.index(phone), phone])

            for number in only_numbers_phone:
                if not number.isdigit():
                    phone_numebers_list_char_error_list_test.append(
                            [phone_list.index(phone), phone]
                    )
    return phone_numebers_list_format_error_list_test, phone_numebers_list_char_error_list_test


def test_phone_format_validator():
    assert phone_format_validator(phone_numebers_list_test) == ([], [])
