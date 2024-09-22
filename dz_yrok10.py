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
responses = {
    '/profile':{
        'method': 'GET',
        'status_code': 200,
         'body': 'success get'
    },
    '/main-page': {
         'method': 'POST',
        'status_code': 201,
        'body': 'success post'
        },
      '/admin': {
      'method': 'GET',
      'status_code': 401,
      'body': 'not authorized'
      },
}
