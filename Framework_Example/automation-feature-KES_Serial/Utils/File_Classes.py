# classes and methods to access read and write to files
import json
import sys
import os
from os import path

class JSON():
    def __init__(self):
        dirname=os.path.dirname(__file__)
        print(dirname)
        self.jsn_path =os.path.join(dirname, 'test_config.json')
        print(self.jsn_path)
        pass

    def check_if_exists(self):
        # check if the path exists return True/False
        path_exists = path.exists(self.jsn_path)
        return path_exists

    def print_json(self):
        with open(self.jsn_path) as json_file:
            data = json.load(json_file)
            data = json.dumps(data, indent=4)
            print(data)
            json_file.close()

    def print_uiVersionString(self, product_type):
        # product_type has to match the product type for the brewer, example 'premium'
        # see teh test_config.json for examples
        with open(self.jsn_path) as json_file:
            data = json.load(json_file)
            # print(data['products'][product_type]['productName'])
            return (data['products'][product_type]['uiVersionString'])
            json_file.close()


    def get_json_paramter(self, product_type, parameter_to_read):
        # get a parameter from the json config file
        with open(self.jsn_path) as json_file:
            data = json.load(json_file)
            return (data['products'][product_type][parameter_to_read])
            json_file.close()

    def set_json_parameter(self, product_type, parameter_to_write, value):
        # set a parameter to a json config file
        with open(self.jsn_path) as json_file:
            # convert json to dictionary format
            data=json.load(json_file)
            # extract a dictionary corresponding to a product_type
            dictionary = data['products'][product_type]
            # update the parameter_to_write, with value passed
            dictionary.update({parameter_to_write : value})
            print("dict: ", dictionary)
            # overwrite the data dictionary at products/product_type with the updated dictionary
            data['products'][product_type] = dictionary
            # print(data)


        with open(self.jsn_path, 'w') as outfile:
            # convert to json format
            json_file = json.dump(data, outfile,indent=4)
            json_file.close()







# # testing
# # init load and print the json file content
# js = JSON()
# print(js.check_if_exists())
# js.print_json()
# # version string
# uiVersionString = js.print_uiVersionString('premium')
# print("version: ", uiVersionString)
# # read a paramter based on the product
# read_parameter = js.get_json_paramter('premium', 'productName')
# print("Selected Parameter: ", read_parameter)
# # read a nested parameter
# serial = js.get_json_paramter('premium', "sandstone")
# comport = serial['comport']
# print('comport', comport)
# # update a parameter in JSON file
# js.set_json_parameter('premium', 'productName', 'K115')

