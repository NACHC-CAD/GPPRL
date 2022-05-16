import main.match.cuda.match_cuda as mc
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("zip1", metavar='<Zip 1 path>', type=str, help='The first zipfile containing hashes')
    parser.add_argument("zip2", metavar='<Zip 2 path>', type=str, help='The second zipfile containing hashes')
    parser.add_argument("threshold", metavar='<Threshold>', type=float, help='The matching threshold')
    parser.add_argument("--outfile", metavar='<Output file path>', type=str, help='The outputfile', default="./results.csv", dest="outfile")
    params = parser.parse_args()
    return params


def match(zip1_name, zip2_name, threshold, outfile):
    mc.match(zip1_name, zip2_name, threshold, outfile)


if __name__ == "__main__":
    args = parse_args()
    match(args.zip1, args.zip2, args.threshold, args.outfile)

