import re
import sys
import os

try:
    main_lua_path = sys.argv[1]
except IndexError:
    print("You didn't pass the correct parameter.")
    exit()


import re

import re

def bump_patch_version(version):
    parts = version.split('.')
    if len(parts) == 2:
        major, minor = parts
        patch = 0
    else:
        major, minor, patch = parts
    return f"{major}.{minor}.{int(patch) + 1}"

def update_file(file_path, pattern, replacement):
    with open(file_path, 'r') as file:
        content = file.read()
    
    updated_content = re.sub(pattern, replacement, content)
    
    with open(file_path, 'w') as file:
        file.write(updated_content)

# Update Main.lua
main_lua_pattern = r'(_version = ")(\d+\.\d+(?:\.\d+)?)(")'

with open(main_lua_path, 'r') as file:
    content = file.read()
    current_version = re.search(main_lua_pattern, content).group(2)

new_version = bump_patch_version(current_version)

update_file(main_lua_path, main_lua_pattern, f'\\g<1>{new_version}\\g<3>')

# Update mod.info
mod_info_path = 'mod.info'
mod_info_pattern = r'(modversion=)(\d+\.\d+(?:\.\d+)?)'

update_file(mod_info_path, mod_info_pattern, f'\\g<1>{new_version}')

print(f"Version bumped to {new_version}")