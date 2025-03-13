import os
import platform
import shutil
FOLDER_PATH = os.path.join(os.path.expanduser("~"), "Downloads")
if not os.path.exists(FOLDER_PATH):
    print(f"Error: The folder {FOLDER_PATH} does not exist.")
    exit(1)  # Exit the script if the folder isn't found
FILE_CATEGORIES = {          # File categories and extensions
    "Images": [".psd", ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".avi", ".mp4", ".mkv", ".mov", ".mts"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".dmg", ".sh"],}
def get_category(extension):
    """*Finds the category for a given file extension.*"""
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Misc"  # Folder for unknown file types
def organize_files():
    """*Organizes files in the specified folder.*"""
    for filename in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, filename)
        
        if os.path.isfile(file_path): 
            ext = os.path.splitext(filename)[1].lower()
            if not ext:  # Skip files when no extension
                continue
            category = get_category(ext)
            category_folder = os.path.join(FOLDER_PATH, category)
            # category folder if it doesn't exist
            os.makedirs(category_folder, exist_ok=True)
            # Avoid overwriting existing files by renaming duplicates
            dest_path = os.path.join(category_folder, filename)
            counter = 1
            while os.path.exists(dest_path):
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_{counter}{ext}"
                dest_path = os.path.join(category_folder, new_filename)
                counter += 1
            shutil.move(file_path, dest_path)
            print(f"Moved {filename} to {category}/")
if __name__ == "__main__":
    organize_files()
