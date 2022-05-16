import csv

import main.util.file.file_util as fu


def create_link_file(src_dir):
    print("Creating link file...")
    print("Dir: " + src_dir)
    print("Files: ")
    file_list = fu.get_files(src_dir)
    out = []
    orgs = {}
    cols = {}
    col_count = get_org_count(file_list)
    print("Creating link file for:")
    for file_name in file_list:
        print("    " + file_name)
    print()
    print("Creating link file...")
    for file_name in file_list:
        create_file(file_name, src_dir, orgs, out, cols, col_count)
    print()
    print("Done creating link file.")
    print()
    print()


def get_org_count(file_list):
    cnt = 1
    size = len(file_list)
    while True:
        cnt = cnt + 1
        size = size - cnt
        if size <= 0:
            return cnt


def create_file(file_name, src_dir, orgs, out, cols, ncols):
    print("Adding file: " + file_name)
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        # get the dictionary for org 1
        org1 = headers[0]
        if org1 not in orgs.keys():
            dic1 = {}
            orgs[org1] = dic1
            cols[org1] = len(cols)
        dic1 = orgs[org1]
        org1_col = cols[org1]
        # get the dictionary for org 2
        org2 = headers[1]
        if org2 not in orgs.keys():
            dic2 = {}
            orgs[org2] = dic2
            cols[org2] = len(cols)
        dic2 = orgs[org2]
        org2_col = cols[org2]
        # read the file
        for line in reader:
            org1_val = int(line[0])
            org2_val = int(line[1])
            if org1_val not in dic1.keys() and org2_val not in dic2.keys():
                new_row = [None]*ncols
                dic1[org1_val] = len(out)
                dic2[org2_val] = len(out)
                new_row[org1_col] = org1_val
                new_row[org2_col] = org2_col
                dic1[org1_val] = len(out)
                dic2[org2_val] = len(out)
                out.append(new_row)
            else:
                if org1_val in dic1:
                    row_num = dic1[org1_val]
                else:
                    row_num = dic2[org2_val]
                out[row_num][org1_col] = org1_val
                out[row_num][org2_col] = org2_val
    # write the file
    out_file = src_dir + "\\" + "link-file.csv"
    with open(out_file, "w", newline="") as f:
        w = csv.writer(f)
        w.writerows(out)





