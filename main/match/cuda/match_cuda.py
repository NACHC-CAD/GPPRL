import main.util.file.file_util as fu
import base64
from zipfile import ZipFile
import json
import subprocess
import csv
import time
import argparse
import os


def match(zip1_name, zip2_name, threshold, out_dir, exe="./dice-gpu-optimized.exe"):
    start = time.time()
    z1 = ZipFile(zip1_name)
    z2 = ZipFile(zip2_name)
    org1 = fu.get_file_prefix_from_path(zip1_name)
    org2 = fu.get_file_prefix_from_path(zip2_name)
    print()
    print("-------------------------------")
    print("Starting match process:")
    print("input1: " + zip1_name)
    print("input2: " + zip2_name)
    print("output: " + out_dir)
    print("Matching on:")
    for path in z1.namelist():
        print("  " + path)
    print("-------------------------------")
    print()
    print()

    results = dict()

    # for each json string (schema) in the zip file
    for path in z1.namelist():
        print("Starting Schema: " + path + "...")

        # get the json string for the first zip
        with z1.open(path) as f:
            j1 = json.load(f)
        # get the json string for the second zip
        with z2.open(path) as f:
            j2 = json.load(f)

        # write the bytes of j1 to a file called dataset1.bin
        bytes_list = [base64.b64decode(x) for x in j1["clks"]]
        with open("./dataset1.bin", "wb") as f:
            for clk in bytes_list:
                f.write(clk)
        # write the bytes of j2 to a file called dataset1.bin
        bytes_list = [base64.b64decode(x) for x in j2["clks"]]
        with open("./dataset2.bin", "wb") as f:
            for clk in bytes_list:
                f.write(clk)

        # run the comparison using the gpu executable
        result = subprocess.run([exe, str(threshold)], cwd=os.getcwd(), capture_output=True, text=True)
        print(result.stdout)

        # update the matches file with any new matches
        with open("./matches.csv", "r") as f:
            r = csv.reader(f)
            for line in r:
                if line[1] != "-1":
                    results[int(line[0])] = int(line[1])

    # write the matches to the results file
    out_file = out_dir + "\\" + org1 + "-" + org2 + "-results.csv"
    with open(out_file, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([org1, org2])
        w.writerows(sorted(results.items(), key=lambda item: item[0]))
    end = time.time()

    os.remove("./matches.csv")
    os.remove("./dataset1.bin")
    os.remove("./dataset2.bin")
    print("Results written to: " + out_file)
    print(f"Finished matching in: {end - start} seconds")
    print()
    print()


