import csv
import os
import main.util.file.file_util as fu


def create_link_file(src_dir):
    # delete any previously created file
    fu.delete(src_dir + "\\" + "link-file.csv")
    # create the link file
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
    # get the column headers
    headers = [None] * len(cols.keys())
    for key in cols.keys():
        val = cols[key]
        headers[val] = key
    # write the file
    out_file = src_dir + "\\" + "link-file.csv"
    with open(out_file, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(headers)
        w.writerows(out)
    print("File created:")
    print(out_file)
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
                # add the roe
                new_row = [None]*ncols
                # add org1 data
                if org1_val != -1:
                    new_row[org1_col] = org1_val
                    dic1[org1_val] = len(out)
                # add org2 data
                if org2_val != -1:
                    new_row[org2_col] = org2_val
                    dic2[org2_val] = len(out)
                out.append(new_row)
            else:
                if org1_val in dic1 and org2_val not in dic2 and org2_val != -1:
                    row_num = dic1[org1_val]
                    out[row_num][org2_col] = org2_val
                if org2_val in dic2 and org1_val not in dic1 and org1_val != -1:
                    row_num = dic2[org2_val]
                    out[row_num][org1_col] = org1_val

    print("done adding file")



