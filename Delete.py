import os

def delete_file(path):
    if not os.path.exists(path):
        print(f"Файл '{path}' не существует.")
        return

    if os.path.isfile(path):
        os.remove(path)
        print(f"Файл '{path}' удалён.")
    else:
        print(f"'{path}' не является файлом.")