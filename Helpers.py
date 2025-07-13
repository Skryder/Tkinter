import re

def find_line_by_keyword_efficient(filename, keyword):
    pattern = rf'{re.escape(keyword)}'
    
    with open(filename, 'r') as file:
        for line in file:
            if re.match(pattern, line):
                return line.strip()
    
    return None

##TODO: create function that takes an already opened file, rather than opening it every time
def find_line_by_keyword(filename, keyword):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if re.match(keyword, line):
                return line
    
    return None


# Usage
#line = find_line_by_keyword('config.txt', 'database_host')
#print(line)  # Output: database_host: localhost