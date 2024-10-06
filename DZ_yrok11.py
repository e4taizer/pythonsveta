# def fio():
#      imia =input("Введите имя:")
#      familiia = input("Введите фамилию:")
#      otchestvo = input("Введите отчество:")
#
# fio()
###dz№1
# def fio ():
#     imia = input("Введите имя:")
#     familiia = input("Введите фамилию:")
#     otchestvo = input("Введите отчество:")
#     print(f" {imia[0].upper()}.{familiia[0].upper()}.{otchestvo[0].upper()}.")
#
# fio()
############## dz №2
######################################
# prodykty = {
#     "spisok_productov": ["яблоко", "апельсин", "Ананас"]
# }
# def dobavlnenie_producta():
#     dob_da_net = input("Добавить продукт? (да/нет): ")
#
#     if dob_da_net.lower() == "да":
#         nazvanie = input("Введите название продукта: ")
#
#
#         if nazvanie.lower() in [product.lower() for product in prodykty["spisok_productov"]]:
#             kolichest = input("Введите количество: ")
#             tsena = input("Введите цену: ")
#         elif nazvanie.lower()  not in [product.lower() for product in prodykty["spisok_productov"]]:
#             prodykty["spisok_productov"].append(nazvanie)
#             print(f"Продукт '{nazvanie}' добавлен в список.")
#         dobavlnenie_producta()
#
#     elif dob_da_net.lower() == "нет":
#         print("Продукт не добавлен.")
#     else:
#         print("Неверный ввод. Введите 'да' или 'нет'.")
#
#
# dobavlnenie_producta()
# print(prodykty)
###############################

prodykty = dict()
def dobavlnenie_producta():
    dob_da_net = input("Добавить продукт? (да/нет): ")

    if dob_da_net.lower() == "да":
        key = input("Введите название продукта: ")


        if key.lower() :
            value = int(input("Введите цену: "))

            kolichestvo = int (input("Введите количество: "))
            prodykty[key] = {"цена": value, "количество": kolichestvo}


        dobavlnenie_producta()

    elif dob_da_net.lower() == "нет":
        for key,data in prodykty.items():
            ctoimost = data["цена"] * data["количество"]
            prodykty[key]["стоимость"] = ctoimost



            print(f'{key},Цена:{data["цена"]},,Количество:{data["количество"]},Стоимость:{ctoimost}')
        total_sum = sum(data["стоимость"] for data in prodykty.values())
        nds = total_sum*20/120
        print(f'Итого:{total_sum}, НДС:{nds:.2f}')

    else:
        print("Неверный ввод. Введите 'да' или 'нет'.")


dobavlnenie_producta()

