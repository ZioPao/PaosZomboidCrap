import sys
import shutil
import os

try:
    user = sys.argv[1]
    workspace = sys.argv[2]      # ${workspaceFolderBasename}
except IndexError:
    print("You didn't pass the correct parameter.")
    exit()

try:
    additional_text = sys.argv[3]
except Exception:
    additional_text = ""


modified_workspace = workspace + additional_text


zomboid_folder = "C:\\Users\\" + user + "\\Zomboid"

mods_folder = os.path.join(zomboid_folder, "mods")
workshop_folder = os.path.join(zomboid_folder, "Workshop")

workshop_mod_root_dir = os.path.join(workshop_folder, modified_workspace)

workshop_mod_contents_dir = os.path.join(workshop_mod_root_dir, "Contents")

# Try to remove old data from contents
try:
    shutil.rmtree(workshop_mod_contents_dir)
except(FileNotFoundError):
    pass

workshop_mod_full_dir = os.path.join(workshop_mod_root_dir, "Contents", "mods", modified_workspace)


os.makedirs(workshop_mod_full_dir, exist_ok=True)



og_mod_folder = os.path.join(mods_folder, workspace)

################# Various locations
media_folder = os.path.join(og_mod_folder, "media")
shutil.copytree(media_folder, os.path.join(workshop_mod_full_dir, "media"), dirs_exist_ok=True)

# Root files
root_files_to_copy = ["workshop.txt", "preview.png"]
for file in root_files_to_copy:
    try:
        path = os.path.join(og_mod_folder, "workshop_files", file)
        shutil.copy(path, workshop_mod_root_dir)
    except Exception:
        print("Error copying " + file)


mod_files_to_copy = ["mod.info", "poster.png", "icon.png"]

for file in mod_files_to_copy:
    try:
        path = os.path.join(og_mod_folder, file)
        shutil.copy(path, workshop_mod_full_dir)
    except Exception:
        print("Error copying " + file)



# todo change mod.info with additional_text

print("All done!")