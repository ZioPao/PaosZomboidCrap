import sys
from getpass import getpass
import subprocess
import os

app_id = "108600"

try:
    published_file_id = sys.argv[1]
    content_folder = sys.argv[2]        # should bestatic
except IndexError:
    print("You didn't pass the correct parameter.")
    exit()



change_note = input("Changenote: ")
os.chdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'steamcmd'))

vdf_content = f'''
"workshopitem"
{{
    "appid" "{app_id}"
    "publishedfileid" "{published_file_id}"
    "contentfolder" "{content_folder}"
    "changenote" "{change_note}"
}}
'''
with open('item.vdf', 'w') as vdf_file:
    vdf_file.write(vdf_content)



username = input("Username: ")
password = getpass()
subprocess.run(f"steamcmd.exe +login {username} {password} +workshop_build_item item.vdf +quit", shell=True)

