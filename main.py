import os
import shutil


path=input("Enter the file path :").strip()

if os.path.exists(path):
    print("path is correct")


    # get all  items in side the folder 
    
    
    items=os.listdir(path)

    # print("The list of items is :")
    # print(items)
                           # filter only files 
    files=[f for f in items if os.path.isfile(os.path.join(path,f))]

    # print("Only files :")
    # print(files)
    
    
     # extrct the extenction


    for file in files:
        name,ext=os.path.splitext(file)


        # remove . dot from extenction
        
        
        ext=ext.replace('.','')
        folder_path=os.path.join(path,ext)

        # mkr folder for each extection
        
        os.makedirs(folder_path,exist_ok=True)

        sourse= os.path.join(path,file)

        distination=os.path.join(folder_path,file)
        shutil.move(sourse,distination)

        print(f"moved :{file} -> {folder_path}")
     


else:
    print("invalid path / path not exist")
