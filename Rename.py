import os
import datetime

def get_date_prefix(file_path):
    creation_time = os.path.getctime(file_path)
    return datetime.datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d")

def rename_file(file_path):
    dir_name = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    date_str = get_date_prefix(file_path)
    new_name = f"{date_str}_{base_name}"
    new_path = os.path.join(dir_name, new_name)

    os.rename(file_path, new_path)
    print(f"Переименован: {file_path} → {new_path}")

def rename_with_date(path, recursive=False):
    if os.path.isfile(path):
        rename_file(path)

    elif os.path.isdir(path):
        if recursive:
            for root, dirs, files in os.walk(path):
                for file in files:
                    full_path = os.path.join(root, file)
                    rename_file(full_path)
        else:
            for file in os.listdir(path):
                full_path = os.path.join(path, file)
                if os.path.isfile(full_path):
                    rename_file(full_path)
    else:
        print(f"Путь не найден: {path}")