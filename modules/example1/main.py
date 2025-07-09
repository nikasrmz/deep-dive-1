print(f'----------- running main.py - {__name__} ----------- ')

import module1

print(module1)
module1.pprint_dict('main.globals', globals())

import module1

# pprint_dict('module1.globals', globals())
    
