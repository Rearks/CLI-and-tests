
import os

def copy_file(source, destination):
    if not os.path.isfile(source):
        raise FileNotFoundError(f"Файл '{source}' не найден")

    with open(source, "rb") as src:
        data = src.read()

    with open(destination, "wb") as dst:
        dst.write(data)

    return f"Файл '{source}' скопирован в '{destination}'"