import main.util.file.file_util as fu


def match_all(input_dir, threshold, output_dir):
    print("Starting match all...")
    print("Input Dir:  " + input_dir)
    print("Output Dir: " + output_dir)
    print("Threshold:  " + str(threshold))
    file_list = fu.get_files(input_dir)
    print("Files: ")
    print(file_list)
    for file_name in file_list:
        print("    " + file_name)

    # do comparisons for each file in the list
    for file_name in file_list:
        if len(file_list) < 2:
            break
        file_name = file_list[0]
        file_list = file_list[1:]
        do_match(file_name, file_list)
    print("Done with match all.")


def do_match(file_name, file_list):
    print("-------------------------------")
    print("STARTING MATCHES FOR: " + file_name)
    print(file_name)
    print(file_list)
    print(len(file_list))
