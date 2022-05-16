import json
import main.util.file.file_util as fu
from zipfile import ZipFile


def get_number_of_patients(zip_file_location):
    z1 = ZipFile(zip_file_location)
    with z1.open(z1.namelist()[0]) as f:
        j1 = json.load(f)
    return len(j1["clks"])


def get_number_of_patients_for_dir(src_dir):
    file_list = fu.get_files(src_dir)
    for file_name in file_list:
        cnt = get_number_of_patients(file_name)
        print(str(cnt) + "\t" + file_name)
    print()
    print("End of file list")
