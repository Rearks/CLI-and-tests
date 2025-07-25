import argparse
from Copy import copy_file
from Delete import delete_file
from Count import count_files_in_folder

def main():
    parser = argparse.ArgumentParser(description="Простой файловый менеджер")
    subparsers = parser.add_subparsers(dest="command")

    # Команда: copy
    copy_parser = subparsers.add_parser("copy", help="Копировать файл")
    copy_parser.add_argument("source", help="Путь к исходному файлу")
    copy_parser.add_argument("destination", help="Путь назначения")

    # Команда: delete
    delete_parser = subparsers.add_parser("delete", help="Удалить файл")
    delete_parser.add_argument("source", help="Файл для удаления")

    # Команда: count
    count_parser = subparsers.add_parser("count", help="Подсчитать файлы в папке")
    count_parser.add_argument("source", help="Папка для подсчета файлов")

    args = parser.parse_args()

    if args.command == "copy":
        message = copy_file(args.source, args.destination)
        print(message)


    elif args.command == "delete":
        delete_file(args.source)

    elif args.command == "count":
        print(f"Количество файлов: {count_files_in_folder(args.source)}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()