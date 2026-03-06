import os
import zipfile

def zip_directory(path, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            # Skip node_modules, .git, and __pycache__
            if 'node_modules' in dirs:
                dirs.remove('node_modules')
            if '.git' in dirs:
                dirs.remove('.git')
            if '__pycache__' in dirs:
                dirs.remove('__pycache__')
            
            for file in files:
                # Skip the zip file itself if it's in the same directory
                if file == os.path.basename(zip_filename):
                    continue
                
                file_path = os.path.join(root, file)
                # Create archive name by removing the base path
                archive_name = os.path.relpath(file_path, path)
                zipf.write(file_path, archive_name)

if __name__ == "__main__":
    source_dir = r"c:\Users\AKSHIDHAABALAJI\Desktop\sustainability_tracker_final"
    destination_zip = r"c:\Users\AKSHIDHAABALAJI\Desktop\final_copy.zip"
    print(f"Zipping {source_dir} to {destination_zip}...")
    zip_directory(source_dir, destination_zip)
    print("Zipping complete!")
