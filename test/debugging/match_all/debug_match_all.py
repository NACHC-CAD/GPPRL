import main.util.file.file_util as fu
import main.match.cuda.match_all_cuda as ma


def debug_match_all():
    print()
    print()
    print("Starting test...")
    input_dir = "D:\\test\\pprl\\gpprl\\smallest"
    output_dir = "D:\\test\\pprl\\gpprl\\smallest\\output"
    fu.rmdir(output_dir)
    fu.mkdirs(output_dir)
    exe = fu.get_file_name("dice-gpu-optimized.exe")
    ma.match_all(input_dir, 0.75, output_dir, exe)
    print("Done.")


if __name__ == "__main__":
    debug_match_all()

