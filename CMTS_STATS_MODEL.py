
import json
import re
import Helpers

class CMTS_STATS_MODEL:

    model = {}
    model_string = ""

    def __init__(self):
        print("hello")

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

    def parse(self, input):
        self.model_string = input

    def parse_from_clipboard(self, input):
        try:
            print("Before Dictification: "+input+"\n")
            self.model = Helpers.dictify(input)
            print("After Dictification: "+str(self.model)+"\n")
        except Exception as e:
            print(e)

    def get_cm_index(self):
        return self.model['CM Index']


#This allows us to initialise and debug the file by itself as if it was main
if __name__ == '__main__':   
    CMTS_STATS_MODEL()



