import re
import json
#from typing import overload

def find_line_by_keyword_efficient(filename, keyword):
    pattern = rf'{re.escape(keyword)}'
    
    with open(filename, 'r') as file:
        for line in file:
            if re.match(pattern, line):
                return line.strip()
    
    return None

def find_line_by_keyword_open_file(filename, keyword): #TODO: refactor this at some point
    with open(filename, 'r') as file:
        ret = ''
        f = 0
        for line in file:
            line = line.strip()
            if re.match(keyword, line):
                match(f): 
                    case 0: 
                        ret = ret + line
                        f = 1
                    case 1: ret = ret + ", " + line
                #print(ret)
            
        if (ret!='' and ret): 
            #print("ret: "+ret)
            return ret
    return None

def find_line_by_keyword(input, keyword):
    ret = ''
    f = 0
    for line in input:
        line = line.strip()
        if re.match(keyword, line):
            match(f): 
                case 0: 
                    ret = ret + line
                    f = 1
                case 1: ret = ret + ", " + line
            #print(ret)
        
    if (ret!='' and ret): 
        #print("false ret: "+ret)
        return ret
    return None


def find_line_by_keyword_new(filename, keyword):
    with open(filename, 'r') as file:
        items=re.findall(keyword, filename, re.MULTILINE) ##what dis do
        for x in items:
            print(x)
    
    
def breakup(self, input):
    ret = ''
    input = input.split(",")
    for items in input:
        ret = ret + self.clean(items)
    return ret

def clean(input):
    input = input.split(":")
    #input[0] = input[0].strip()
    input[1] = input[1].strip("\r\n")
    #input[1] = input[1].strip()
    return input[1]

def dictify(input):
    dict = {}
    input = input.split("\n")
    for line in input:
        #Removes all duplicate whitespace
        line = ' '.join(line.split())
        line = line.strip()
        if(line.find(":") > 0):
            linelist = line.split(":")
            linelist[0] = linelist[0].strip()
            linelist[1] = linelist[1].strip()
            if(linelist[1].find(" ") > 0): #If there are multiple values (E.g upstream SNR)
                linelist[1] = linelist[1].split(" ") #split it into a list
            if(dict.get(linelist[0])): #If there are multiple lines with the same type of data (E.g any downstream stat)
                linelist[1] = dict.get(linelist[0]) + linelist[1] #append the data to the already existing key rather than overwriting it
            dict[linelist[0]] = linelist[1]
    return dict

# Usage
#line = find_line_by_keyword('config.txt', 'database_host')
#print(line)  # Output: database_host: localhost