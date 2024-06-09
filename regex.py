import re

regex = 'Mã lớp:\s([A-Z]+[0-9]+)\s?$'

with open('init_class.txt','r',encoding='utf-8') as file:
    l = file.readlines()
    for line in l:
        match = re.match(regex,line)
        if match:
            print(match.group(1))
