import unittest
import os
from Copy import copy_file
from Delete import delete_file
from Count import count_files_in_folder

class TestUtils(unittest.TestCase):
    def setUp(self):
        with open("testfile.txt", "w") as f:
            f.write("Тестовый файл")

    def tearDown(self):
        for f in ["testfile.txt", "copy.txt"]:
            if os.path.exists(f):
                os.remove(f)

    def test_copy_file_success(self):
        msg = copy_file("testfile.txt", "copy.txt")
        self.assertTrue(os.path.exists("copy.txt"))
        self.assertIn("скопирован", msg)

    def test_copy_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            copy_file("не_существует.txt", "copy.txt")


class TestDeleteFile(unittest.TestCase):
    def setUp(self):
        self.test_file = "temp_test_file.txt"
        with open(self.test_file, "w") as f:
            f.write("тест")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_delete_existing_file(self):
        self.assertTrue(os.path.exists(self.test_file))
        delete_file(self.test_file)
        self.assertFalse(os.path.exists(self.test_file))

    def test_delete_nonexistent_file(self):
        fake_file = "nonexistent_file.txt"
        self.assertFalse(os.path.exists(fake_file))
        delete_file(fake_file)


class TestCountFiles(unittest.TestCase):
    def setUp(self):
        os.makedirs("testdir/subfolder", exist_ok=True)
        with open("testdir/a.txt", "w") as f:
            f.write("A")
        with open("testdir/b.txt", "w") as f:
            f.write("B")
        with open("testdir/subfolder/c.txt", "w") as f:
            f.write("C")

    def tearDown(self):
        for root, dirs, files in os.walk("testdir", topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir("testdir")

    def test_count_files(self):
        count = count_files_in_folder("testdir")
        self.assertEqual(count, 3)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)