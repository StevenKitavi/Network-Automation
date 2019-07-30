import yaml
from pprint import pprint

def ly(filename):
    with open(filename) as _:
        return yaml.load(_)

print(ly('1-list.yml'))