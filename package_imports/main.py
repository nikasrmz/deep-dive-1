# import common
import common.validators

print(common)

import common.validators.boolean as boolean

print(boolean.boolean_helper_1)

def importer():
    import common.module1

print("imported")

importer()
