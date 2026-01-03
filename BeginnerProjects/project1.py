

from pathlib import Path
folder = Path("/AutomationProjects/BeginnerProjects/BulkFileRenamer/AutomationDir")

c=1
for file in folder.iterdir():
    #print(c,file)
    #c+=1

    #print(file.suffix)
    new_name = f"automation_{c}{file.suffix}"
    #print(file, "->", new_name)
    file.rename(file.with_name(new_name))
    print("Renamed:", new_name)
    c+=1
