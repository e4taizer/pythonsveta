####
#dz№1
# words = {
#     "Noon":"Noon",
#     "cat":"rat",
#     "Кот":"Ток",
#     "загон":"гаЗон"
# }
# for key,value in words.items():
#     key_clean = key.replace(" ", "").lower()
#     value_clean = value.replace(" ", "").lower()
#     is_palindrome = key_clean == key_clean[::-1] and value_clean == value_clean[::-1]
#     is_anagram = sorted(key_clean) == sorted(value_clean)
#     print(f"Слова '{key}' и '{value}' {'являются' if is_palindrome else 'не являются'} палиндромами "
#       f"и {'являются' if is_anagram else 'не являются'} анаграммами.")
####
# dz#2
# responses = {
#     '/profile':{
#         'method': 'GET',
#         'status_code': 200,
#          'body': 'success get'
#     },
#     '/main-page': {
#          'method': 'POST',
#         'status_code': 201,
#         'body': 'success post'
#         },
#       '/admin': {
#       'method': 'GET',
#       'status_code': 401,
#       'body': 'not authorized'
#       },
# }
#
# # for key,value in responses.items():
# #     for sub_key, sub_value in value.items():
# #         if sub_key == 'status_code' and  200 <= sub_value < 300:
# #             print(f"{sub_key} и {sub_value}")
# vse_proshli = all(200 <=value['status_code'] <300 for value in responses.values())
# if vse_proshli:
#     print('passed')
# else:
#   print('failed')
#
# for endpoint,value  in responses.items():
#     if not(200<=value['status_code'] <300):
#         print(f"{endpoint} имеет код {value['status_code']}, который вышел за пределы диапазона")
##############№3
