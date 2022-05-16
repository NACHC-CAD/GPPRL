import main.util.file.file_util as fu


def test_get_file_name():
    print()
    print()
    print("Starting test...")
    rel_path = "./test_file_util.py"
    file_path = fu.get_file_name(rel_path)
    print("File Path:   " + file_path)
    file_name = fu.get_file_name_from_path(file_path)
    print("File Name:   " + file_name)
    file_prefix1 = fu.get_file_prefix(file_name)
    print("File Prefix: " + file_prefix1)
    file_prefix2 = fu.get_file_prefix_from_path(file_path)
    print("File Prefix: " + file_prefix2)
    print("Done.")


if __name__ == "__main__":
    test_get_file_name()
