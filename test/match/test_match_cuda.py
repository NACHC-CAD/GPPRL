import main.match.cuda.match_cuda as mc
import main.util.file.file_util as fu


def test_match_cuda():
    print("Starting test...")
    zip1_name = fu.get_file_name("test/resources/ncceh.zip")
    zip2_name = fu.get_file_name("test/resources/ymca.zip")
    out = fu.get_file_name("test/output/results.csv")
    exe = fu.get_file_name("dice-gpu-optimized.exe")
    print("zip1: " + zip1_name)
    print("zip2: " + zip2_name)
    print("out:  " + out)
    print("exe:  " + exe)
    mc.match(zip1_name, zip2_name, 0.75, out, exe)
    print("Done.")


if __name__ == "__main__":
    test_match_cuda()

