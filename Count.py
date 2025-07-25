import os

def count_files_in_folder(path):
    count = 0
    for root, dirs, files in os.walk(path):
        count += len(files)
    return count