import shutil

def backup_script (source_folder, backup_folder):
    try:
        shutil.copy(source_folder, backup_folder)
        print(f"Backup složky {source_folder} byl úspěšně vytvořen v {backup_folder}") 
    except Exception as e:
        print(f"Chyba při vytváření zálohy: {e}")

source_path = input("Enter the path of the folder you want to backup: ")
backup_path = r"C:\Users\alesb\Desktop\projects"

backup_script(source_path, backup_path)