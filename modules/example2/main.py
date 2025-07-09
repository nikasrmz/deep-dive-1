import os
import sys
import types

mod_name = 'module1'
mod_file_name = 'module1_source.py'
mod_path = 'modules/example2/'
mod_rel_path = os.path.join(mod_path, mod_file_name)
mod_abs_path = os.path.abspath(mod_rel_path)

# print(mod_rel_path)
# print(mod_abs_path)

with open(mod_rel_path, 'r') as code_file:
    source_code = code_file.read()

# print(source_code)
mod = types.ModuleType(mod_name)
mod.__file__ = mod_abs_path

sys.modules[mod_name] = mod

code = compile(source_code, filename=mod_abs_path, mode='exec')

exec(code, mod.__dict__)

import module1
module1.hello()

print("module1 and mod are the same: ", (module1 is mod))
