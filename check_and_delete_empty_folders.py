import os
path = "/home/salal/saad/dataset/training/all_combined_dataset/output/output_split/test"
obj = os.scandir(path)

for entry in obj:
    if entry.is_dir():
        if not os.listdir(entry):
            print(entry.name)
            os.rmdir(entry)
            

#this code finds an empty directory and removes it
