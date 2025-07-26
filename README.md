### CLI-and-tests  
Структура проекта:  
CLI-and-tests/  
+ Copy.py            # Копирование файлов  
+ Delete.py          # Удаление файлов  
+ Count.py           # Подсчёт файлов  
+ Manager.py         # Основной CLI-интерфейс  
+ test_utils.py      # Тесты для функций  
+ test.txt           # Тестовый файл (можно удалить)  


### Использование:  
**Команда которая позволяет копировать файл:**  
python Manager.py copy путь_к_файлу путь_копии  
  **Пример:**  
   `<python Manager.py copy test.txt copy_test.txt?>`  
**Команда которая удаляет файл:**  
python Manager.py delete путь_к_файлу  
  **Пример:**  
  `<python Manager.py delete copy_test.txt>`   
**Команда подсчитывающая количество файлов в папке:**  
python Manager.py count путь_к_папке  
  **Пример:**  
  `<python Manager.py count my_folder>`   

**Запуск тестов:**  
Файл test_utils.py содержит тесты всех функций.  
**Запуск:**  
`<python test_utils.py>`   

### Автор  
Алексей Скрипкин
