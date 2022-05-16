import glob
import os

src_dir = "../resources/*.zip"

file_list = glob.glob(pathname=src_dir)
print(file_list)

print(os.getcwd())
