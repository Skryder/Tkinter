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

def jsonify(input):
    input = input.split("\n")
    for line in input:
        line = ' '.join(line.split())
        line = line.strip()
        linelist = line.split(":")
        linelist[0] = "\"" + linelist[0].strip() + "\""
        print(linelist[0])
#        linelist[1] = linelist[1].split(" ")
#        linetwo = ''
#        for subline in linelist[1]:
#            subline = "\"" + subline + "\""
#            linetwo = linetwo + subline
        linelist[1] = "\"" + linelist[1].strip() + "\""   
        print(linelist[1])  
        line = linelist[0].join(linelist[1])
        print(line)
    

# Usage
#line = find_line_by_keyword('config.txt', 'database_host')
#print(line)  # Output: database_host: localhost