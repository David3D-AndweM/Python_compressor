import os
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    try:
        if compress_type == 'zip':
            with zipfile.ZipFile(f"{folder_path}_{datetime.now().strftime('%Y_%m_%d')}.zip", 'w') as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), arcname=file)
            print(f"Folder '{folder_path}' compressed as a .zip file.")
        elif compress_type == 'tar':
            with tarfile.open(f"{folder_path}_{datetime.now().strftime('%Y_%m_%d')}.tar", 'w') as tarf:
                tarf.add(folder_path, arcname=os.path.basename(folder_path))
            print(f"Folder '{folder_path}' compressed as a .tar file.")
        elif compress_type == 'tgz':
            with tarfile.open(f"{folder_path}_{datetime.now().strftime('%Y_%m_%d')}.tgz", 'w:gz') as tgzf:
                tgzf.add(folder_path, arcname=os.path.basename(folder_path))
            print(f"Folder '{folder_path}' compressed as a .tgz file.")
        else:
            print("Unsupported compression type.")
    except Exception as e:
        print(f"Compression failed: {e}")

def main():
    folder_path = input("Enter folder path: ")
    print("1. zip")
    print("2. tar")
    print("3. tgz")
    selection = input("Enter selection: ")
    compress_types = { '1': 'zip', '2': 'tar', '3': 'tgz' }
    selected_compress_type = compress_types.get(selection)
    
    if selected_compress_type:
        compress_folder(folder_path, selected_compress_type)
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()
