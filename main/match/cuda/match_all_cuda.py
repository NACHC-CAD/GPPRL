import main.util.file.file_util as fu
import main.match.cuda.match_cuda as mc


def match_all(input_dir, threshold, output_dir, exe):
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
        do_match_all(file_name, file_list, threshold, output_dir, exe)
    print("Done with match all.")


def do_match_all(file_name, file_list, threshold, output_dir, exe):
    print()
    print()
    print("-------------------------------")
    print("STARTING MATCHES FOR: " + file_name)
    for file2_name in file_list:
        do_match(file_name, file2_name, threshold, output_dir, exe)


def do_match(file1_name, file2_name, threshold, output_dir, exe):
    mc.match(file1_name, file2_name, threshold, output_dir, exe)

