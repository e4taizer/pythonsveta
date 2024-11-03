# import xml.etree.ElementTree as ET
# tree = ET.parse("country_data.xml")
# root =tree.getroot()
# print(type(root))
# print(root.tag)
# print(root.attrib)
# for child in root:
#     print(child.tag,child.attrib)
# for neighbor in root.iter("neighbor"):
#     print(neighbor.attrib)
###############
# for country in root.findall("country"):
#     rank =country.find("rank").text
#     name =country.get("name")
#     print(name,rank)
############## Поиск с помощью Xpath
# rank = root.findall(".country/rank")
# for i in rank:
#     print(i.text)
# find и  findall. find выведет только первый элемент
#######
# import csv
# import os
#вывод значений из файла csv
# with open("table.csv",encoding='utf-8') as f:
#     file_reader = csv.reader(f)
#     for row in file_reader:
#         print(row)
#
# with open("table.csv",encoding='utf-8') as f:
#     file_reader = csv.DictReader(f,delimiter=",")
#     for row in file_reader:
#         print(row)
##### Запись в csv  файл
# import json
# data = {
#     "Model":
#         {"type":"car",
#          "speed":180,
#          "gas":95
#          },
#     "Included":("W Jetta","ford Mustang","Mini Cooper")
# }
# with open('car.json', "w+") as file:
#     json.dump(data,file)
# with open("car.json","r") as file:
#     json_string = file.read()
# data = json.loads(json_string)
# print(data)
# print(type(data))