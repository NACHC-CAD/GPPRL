import time

import main.match.cuda.match_all_cuda as ma
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("input_dir", metavar='<Input Dir>', type=str, help='Directory containing zip files')
    parser.add_argument("threshold", metavar='<Threshold>', type=float, help='The matching threshold')
    parser.add_argument("output_dir", metavar='<Output Dir>', type=str, help='Where the output will be written')
    parser.add_argument("exe", metavar='<Executable>', type=str, help='Path to the executable')
    params = parser.parse_args()
    return params


def match_all(input_dir, threshold, output_dir, exe):
    start = time.time()
    ma.match_all(input_dir, threshold, output_dir, exe)
    print()
    print()
    print("Total Elapsed Time: " + str(time.time() - start))
    print("DONE!")
    print()
    print()

if __name__ == "__main__":
    args = parse_args()
    match_all(args.input_dir, args.threshold, args.output_dir, args.exe)

