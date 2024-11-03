import os
import os.path
import json
#os.mkdir("jsnfor_DZ_15")  создали папку
def read_write():
    old_filename ="jsnfor_DZ_15/jsn.json"
    name,ext = os.path.splitext(old_filename)
    new_filename= f"{name}_test{ext}"
    with open(old_filename,"r",encoding='utf-8') as file:
      data_from_file = json.load(file)

    def iter_json_bool(data):
        for key,value in data.items():
             if isinstance(value,bool):
               data[key] = not value
             elif isinstance(value,dict):
              iter_json_bool(value)
             elif isinstance(value,list):
                 for index,element in enumerate(value):

                    if  isinstance(element,bool):
                      value[index]= not  element

                 for item in value:
                     if isinstance(item,dict):

                       iter_json_bool(item)

    iter_json_bool(data_from_file)
    def iter_json_str(data):
        for key,value in data.items():
            if isinstance(value,str):
                data[key] +="_test"
            elif isinstance(value,dict):
                iter_json_str(value)
            elif isinstance(value,list):
                for index,element in enumerate(value):
                    if isinstance(element,str):
                        value[index] +="_test"
                for item in value:
                    if isinstance(item,dict):
                        iter_json_str(item)
    iter_json_str(data_from_file)

    def iter_json_int(data):
        for key,value in data.items():
            if isinstance(value,(int,float)) and not isinstance(value, bool):
                str_value = str(value)
                new_value= "1111"+ str_value

                if isinstance(value,float):
                    data[key]= float(new_value)
                else:
                    data[key]=int(new_value)


            elif isinstance(value,list):


                for index,element in enumerate(value):
                    if isinstance(element,(int,float)) and not isinstance(element, bool):
                        str_value2 = str(element)
                        new_value2 = "1111" + str_value2

                        if isinstance(element, float):
                            value[index] = float(new_value2)
                        else:
                         value[index]= int(new_value2)

                    elif isinstance(element, dict):
                        iter_json_int(element)

               # for item in value:
                   # if isinstance(item,dict):
                       # iter_json_int(item)
  #  iter_json_int(data_from_file)

            elif isinstance(value, dict):
                iter_json_int(value)

    iter_json_int(data_from_file)
    with open(new_filename,"w") as file_test:
       json.dump(data_from_file,file_test)

read_write()

