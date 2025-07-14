import sys
import shutil
import os

try:
    version = sys.argv[1]
    user = sys.argv[2]
    workspace = sys.argv[3]      # ${workspaceFolderBasename}
    test = sys.argv[4]          
except IndexError:
    print("You didn't pass the correct parameter.")
    exit()



zomboid_path = os.path.join("C:\\", "Users", user, "Zomboid")
mods_path = os.path.join(zomboid_path, "mods")
workshop_path = os.path.join(zomboid_path, "Workshop")
workshop_mod_root_path = os.path.join(workshop_path, workspace)


# Clean old Workshop folder
try:
    shutil.rmtree(workshop_mod_root_path)
except(FileNotFoundError):
    pass

workshop_mod_contents_path = os.path.join(workshop_mod_root_path, "Contents")
workshop_mod_main_path = os.path.join(workshop_mod_contents_path, "mods", workspace)
os.makedirs(workshop_mod_main_path, exist_ok=True)


og_mod_path = os.path.join(mods_path, workspace)

# Handle root files
if test == 'test':
    root_files_to_copy = ["workshop_test.txt", "preview.png"]
else:
    root_files_to_copy = ["workshop.txt", "preview.png"]
for file in root_files_to_copy:
    try:
        path = os.path.join(og_mod_path, "workshop_files", file)

        if file == 'workshop_test.txt':
            shutil.copy(path, os.path.join(workshop_mod_root_path, "workshop.txt"))
        else:
            shutil.copy(path, workshop_mod_root_path)
    except Exception:
        print("Error copying " + file)

# mod_files_to_copy = ["poster.png", "icon.png"]
# if version == '41':
#     mod_files_to_copy.append('mod.info')

# for file in mod_files_to_copy:
#     try:
#         path = os.path.join(og_mod_path, file)
#         shutil.copy(path, workshop_mod_main_path)
#     except Exception:
#         print("Error copying " + file)



 # Poster and icon are always the same and are in the root folder.
mod_files_to_copy = ["poster.png", "icon.png"]     
def transfer_files_to_workshop_folder(dest):
    # Copy various miscellaneous files

    for file in mod_files_to_copy:
        try:
            path = os.path.join(og_mod_path, file)
            shutil.copy(path, os.path.join(workshop_mod_main_path, dest))
        except Exception as e:
            print(e)


if version == '42':
    for folder in os.listdir(og_mod_path):
        if folder.startswith("42"):
            folder_path = os.path.join(og_mod_path, folder)
            dest = os.path.join(workshop_mod_main_path, folder)
            shutil.copytree(folder_path, dest, dirs_exist_ok=True)
            transfer_files_to_workshop_folder(dest)
elif version == '41':
    transfer_files_to_workshop_folder(workshop_mod_main_path)

    mod_41_info_path = os.path.join(og_mod_path, "mod_41.info")
    shutil.copy(mod_41_info_path, os.path.join(workshop_mod_main_path, "mod.info"))


# Copy the main content
og_mod_media_folder = os.path.join(og_mod_path, "common", "media")

if version == '42':
    workshop_dest = os.path.join(workshop_mod_main_path, "common", "media")
elif version == '41':
    workshop_dest = os.path.join(workshop_mod_main_path, "media")

shutil.copytree(og_mod_media_folder, os.path.join(workshop_mod_main_path, workshop_dest), dirs_exist_ok=True)