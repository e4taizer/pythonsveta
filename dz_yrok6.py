# product = float(input('Введите число:'))
# if product >= 10:
#     print('Все хорошо')
# else:
#     print ('Все плохо')
########################################
# number = input()
# result = True if len(str(number)) == 2 and str(number)[0] == str(number)[1]  else False
# print("Да" if result else "Нет")
####################################################
#status_code
#response        #stroka
format_type= str(input("format_type:")) #tip dannyx
status_code = int(input("status_code:"))
response  = str(input("Введите фамилии:"))
if format_type =="JSON" or format_type == "":
    print("Postman")
elif format_type == "XML":
    print("SoapUI")
else:
    print ("формат данных не определен")
if status_code ==200:
        print("ok")
elif status_code ==500:
    print("Internal server error")
elif status_code == 400:
    print("Bad Request")


