import base64
from zipfile import ZipFile
import json
import subprocess
import csv
import time
import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("zip1", metavar='<Zip 1 path>', type=str, help='The first zipfile containing hashes')
    parser.add_argument("zip2", metavar='<Zip 2 path>', type=str, help='The second zipfile containing hashes')
    parser.add_argument("threshold", metavar='<Threshold>', type=float, help='The matching threshold')
    parser.add_argument("--outfile", metavar='<Output file path>', type=str, help='The outputfile', default="./results.csv", dest="outfile")
    params = parser.parse_args()
    return params


def match(zip1_name, zip2_name, threshold, outfile):
    start = time.time()
    z1 = ZipFile(zip1_name)
    z2 = ZipFile(zip2_name)
    print("----------------------------------------------------")
    print("Starting match process:")
    print("input1: " + zip1_name)
    print("input2: " + zip2_name)
    print("output: " + outfile)
    print("Matching on:")
    for path in z1.namelist():
        print("  " + path)
    print("----------------------------------------------------")
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
        with open("dataset1.bin", "wb") as f:
            for clk in bytes_list:
                f.write(clk)
        # write the bytes of j2 to a file called dataset1.bin
        bytes_list = [base64.b64decode(x) for x in j2["clks"]]
        with open("dataset2.bin", "wb") as f:
            for clk in bytes_list:
                f.write(clk)

        # run the comparison using the gpu executable
        result = subprocess.run(["./dice-gpu-optimized.exe", str(threshold)], cwd=os.getcwd(), capture_output=True, text=True)
        print(result.stdout)

        # update the matches file with any new matches
        with open("./matches.csv", "r") as f:
            r = csv.reader(f)
            for line in r:
                if line[1] != "-1":
                    results[int(line[0])] = int(line[1])

    # write the matches to the results file
    with open(outfile, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["dataset 1", "dataset 2"])
        w.writerows(sorted(results.items(), key=lambda item: item[0]))
    end = time.time()

    os.remove("./matches.csv")
    os.remove("./dataset1.bin")
    os.remove("./dataset2.bin")
    print("Results written to: " + outfile)
    print(f"Finished matching in: {end - start} seconds")


if __name__ == "__main__":
    args = parse_args()
    match(args.zip1, args.zip2, args.threshold, args.outfile)

