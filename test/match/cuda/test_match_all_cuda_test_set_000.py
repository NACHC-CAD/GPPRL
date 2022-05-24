import time
import main.util.file.file_util as fu
import main.match.cuda.match_all_cuda as ma


def test_match_all():
    print()
    print()
    print("Starting test...")
    start = time.time()
    input_dir = fu.get_file_name("test/resources/test-set-000")
    output_dir = fu.get_file_name("test/output/match-all-test-000")
    fu.mkdirs(output_dir)
    exe = fu.get_file_name("dice-gpu-optimized.exe")
    ma.match_all(input_dir, 0.75, output_dir, exe)
    end = time.time()
    elapsed = end - start
    print("Total Elapsed: " + str(elapsed))
    print("Done.")


if __name__ == "__main__":
    test_match_all()

