import os
import shutil
from pathlib import Path

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# IMPORTANT: SET THE FOLDER YOU WANT TO CLEAN UP!
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# Use 'r' before the string on Windows, e.g., r"C:\Users\YourName\Downloads"
# On Mac/Linux, it might be: "/Users/YourName/Downloads"
#
# *** START BY CREATING A 'test_folder' ON YOUR DESKTOP TO BE SAFE ***
#
TARGET_FOLDER = Path("/Users/YourName/Desktop/test_folder")
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

# 1. Define where file types should go.
# (You can add any new types you want!)
FILE_EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Video": [".mp4", ".mov", ".avi", ".mkv"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

def organize_folder(folder_path):
    """
    Sorts files in the target folder into subdirectories based on extension.
    """
    print(f"Organizing files in: {folder_path}\n")
    
    # 2. Loop through every file in the target folder.
    for item in folder_path.iterdir():
        # 3. Ignore subfolders and hidden files.
        if item.is_dir() or item.name.startswith('.'):
            continue
            
        # 4. Get the file extension (e.g., '.txt')
        file_suffix = item.suffix.lower()
        
        # 5. Find which folder it belongs to.
        destination_folder = None
        for folder_name, extensions in FILE_EXTENSIONS.items():
            if file_suffix in extensions:
                destination_folder = folder_path / folder_name
                break
                
        # 6. If it's a known type, move it.
        if destination_folder:
            # Create the destination folder if it doesn't exist
            destination_folder.mkdir(exist_ok=True)
            
            # Move the file
            try:
                shutil.move(str(item), str(destination_folder))
                print(f"Moved: {item.name}  ->  {destination_folder.name}/")
            except Exception as e:
                print(f"Error moving {item.name}: {e}")
                
        # 7. If it's an "other" type, move it to an 'Other' folder.
        else:
            other_folder = folder_path / "Other"
            other_folder.mkdir(exist_ok=True)
            try:
                shutil.move(str(item), str(other_folder))
                print(f"Moved: {item.name}  ->  Other/")
            except Exception as e:
                print(f"Error moving {item.name}: {e}")

# --- This is where the program starts ---
if __name__ == "__main__":
    if not TARGET_FOLDER.exists() or not TARGET_FOLDER.is_dir():
        print(f"Error: The folder '{TARGET_FOLDER}' does not exist.")
        print("Please check the 'TARGET_FOLDER' variable in the script.")
    else:
        organize_folder(TARGET_FOLDER)
        print("\n✅ All done! Folder is organized.")
