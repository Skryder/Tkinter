
import json
import re
import Helpers

class CMTS_STATS_MODEL:

    model = {}

    def __init__(self):
        #self.parse_from_file('test.txt')
        pass


    def parse_from_file(self, filename):
        
        try:
            file = open(filename, mode = 'r', encoding = 'utf-8-sig')
            input = file.readlines()
            ##file.close()
            model = Helpers.dictify(input)
            print(model)
        except Exception as e:
            print(e)
        finally:
            file.close()


    def parse_from_clipboard(self, input):
        try:
            self.model = Helpers.dictify(input)
        except Exception as e:
            print(e)

    def get_cm_index(self):
        return self.model['CM Index']




        
CMTS_STATS_MODEL()



