import requests
import pprint
import json


class Rest_API_Class():
    def __init__(self, url):
        # define a rest interface, may need more inputs tbd.
        self.url = url

    def import_file(self, file_name):
        # returns a class of the file referenced in the by self.url and a file name
        # if it's a json file it needs to be converted by the .json() method
        file_url = "{0}/{1}".format(self.url, file_name)
        imported_file = requests.get(file_url)
        return imported_file


# # testing
#
# rac = Rest_API_Class(
#     'http://nexusrepo.gmcr.com:9081/nexus/content/repositories/brewerReleases/premium/v1.1.1/Bld-96/SandStone/')
#
# # get the file from nexus
# metadata = rac.import_file('metadata.json')
# # print(type(metadata))
# # print(metadata.json())
# # convert the file to json format
# metadata_json = metadata.json()
# pprint.pprint(metadata_json)
# # extract desired uiVersionString from the file
# target_uiVersionString = metadata_json['uiVersionString']
# print (target_uiVersionString)
