import yaml
from pprint import pprint

def ly(filename):
    with open(filename) as _:
        return yaml.load(_)

#print the list in the 1-list.yml 
my_list = ly('1-list.yml')
print(my_list)


#print the dictionary.yml using the python script
my_dict = ly('dictionary.yml')
for k, v in my_dict.items():
    print (v)

