from pathlib import Path
folder = Path('/Users/preetipalakkaur/PersonalProjects/DataAnalyticsPython/AutomationProjects/BeginnerProjects/automation_sort_test')


for file in folder.iterdir():
    v = {
        ".pdf": "others",
        ".png": "image",
        ".jpg": "image",
        ".mp3": "music",
        ".xlsx": "others",
        ".txt": "others"
    }
    if file.suffix in v:
        #print(file, "->", v[file.suffix])
        target_dir = folder / v[file.suffix]
        target_dir.mkdir(exist_ok=True)

        file.rename(target_dir / file.name)

        print("Moved:", file.name, "to:", target_dir)

