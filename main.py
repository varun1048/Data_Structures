from test import *
from  locate_card import *
import os
os.system('cls')

for x in tests:

    result = locate_card(
        x['inputs']['cards'],
        x['inputs']['query']
        )
 

    output(tests.index(x),result,x['output'])

