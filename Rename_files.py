import os

def rename_files(folder_path):
    files = os.listdir(folder_path)
    num_files = len(files)
    
    for i, filename in enumerate(files, start=1):
        # Get the file extension
        _, ext = os.path.splitext(filename)
        
        # New filename: <index>.<extension>
        new_filename = f"{i}{ext}"
        
        # Construct the new path
        new_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(os.path.join(folder_path, filename), new_path)

if __name__ == "__main__":
    folder_path = "E:\\fotos\\IJSBA WORLD FINALS HAVASU 2023\\fotos LISTAS havasu\\128D5600"  # Replace with your folder path
    rename_files(folder_path)
