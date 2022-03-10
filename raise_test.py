# tel = '(31) 9913-82787'
# filtered_phones = tel[1:3] + tel[5:9] + tel[10:15]
# print(filtered_phones)

# # todo Faz essa mesma coisa que fiz no cpf para telefone e as datas lá
# a = '123.456.789-25'
# b = '{}.{}.{}-{}'.format(a[:3], a[4:7], a[8:11], a[12:15])
# print(b)
# print(a[12:15])
# print(a == b)

# a = 10
# b = 'Lev1i da Cunha'
# lista = []
# for x in b:
#     if x.isdigit():
#         print(x)
#         print('é')
# try:
#     print(a == int(b))
# except ValueError:
#     print(f'O valor {b} está incorreto.')
#     lista.append(b)
#     print(lista)
# # def make_pretty(func):
# #     def inner(a, b):
#         a = a * a
#         b = b * b
#         lista = [a, b]
#         print("I got decorated")
#         func(a, b)
#         return lista
#
#     return inner
#
# #
# @make_pretty
# def ordinary(a, b):
#     print(a * b)


def name_length(func):
    lista1 = []

    def inner(lista):
        error_list = []
        for x in lista:
            lista1.append(x)
        for x in lista1:
            if len(x) > 25:
                error_list.append([x, lista1.index(x)])
        func(error_list)

    return inner


@name_length
def names(lista):
    error_names = lista
    print(error_names)


listaa = ['Kaique', 'lllllllllllllllllllllllllll', 'ddddddddddddddddddddddddddddddddd']
names(listaa)
# ordinary(10, 15)
