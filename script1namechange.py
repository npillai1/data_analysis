import os
counter = 0
path = r"C:\Users\ryanp\OneDrive - University of Maryland\Desktop\labview\11-9-23-Scitech-delta-orificediam-lengths\11-9-23-smallvol-5p22in-quarternptOD-novolchange\test"
files = [] 

os.chdir(path)

for file_name in os.listdir (path):
    if "abc" in file_name:
        old_name = file_name
        new_name = file_name.replace ("abc", "replaced")
        counter += 1
        files.append (new_name)
        os.rename (old_name, new_name)
print (counter)
print (files)

print("end")

