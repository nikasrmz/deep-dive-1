print(f'----------- running {__name__} ----------- ')

def pprint_dict(header, d):
    print('\n-----------------------------------------')
    print(f'****** {header} ******')
    for key, value in d.items():
        print(key, '=', value)
    print('-----------------------------------------\n') 


pprint_dict('module1.globals', globals())
    
