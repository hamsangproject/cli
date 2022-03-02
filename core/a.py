from pprint import pprint
from sys import argv
from dbmanager import get_meaning
print(get_meaning(argv[1], json_out=True))
