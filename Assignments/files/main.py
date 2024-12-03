# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line

# import modules
import os
import shutil
from zipfile import ZipFile

base_path = os.getcwd()
cache_path = os.path.join(base_path, "cache")
data_path = os.path.join(base_path, "data.zip")

# 1 :function clean_cache.

def clean_cache():
    #cache_path = "files\cache"

    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)

    os.makedirs(cache_path)
    print("Cache folder has been cleaned.")

# 2 : function cache_zip.

def cache_zip(zip_path, cache_path):
    with ZipFile(zip_path, 'r') as datazip:
        datazip.extractall(cache_path)
    print("Zip file has been unpacked into the cache folder.")

# 3 : function cached_files.

def cached_files():
    #cache_directory = "files\cache"
    file_paths = []
    for root, dirs, files in os.walk(cache_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(os.path.abspath(file_path))
    return file_paths

# 4 : function find_password.

def find_password(file_paths):
    password_indicator = "password"

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
            if password_indicator in content:
                password_start_index = content.index(password_indicator) + len(password_indicator) + 1
                password = content[password_start_index:].split()[0]
                return password

    return None

# Clean the cache folder
clean_cache()

# cache the zip file.
cache_zip(data_path, cache_path)


# Get the list of file paths in the cache
files = cached_files()

# Find the password in the files
password = find_password(files)

if password:
   print(f"The password is: {password}")
else:
    print("Password not found.")


