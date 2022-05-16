import main.util.file.file_util as fu


def create_link_file(src_dir):
    print("Creating link file...")
    print("Dir: " + src_dir)
    print("Files: ")
    file_list = fu.get_files(src_dir)
    for file_name in file_list:
        print("    " + file_name)
    print()
    print("Done creating link file.")
    print()
    print()
