import main.util.file.file_util as fu
import main.match.cuda.util.create_link_file as link


def test_create_link_file():
    print()
    print()
    print("Starting test...")
#    src_dir = fu.get_file_name("test/resources/match-results/test-set-from-smallest-three")
#    src_dir = fu.get_file_name("test/resources/match-results/simple-test-set")
    src_dir = "C:\\test\\pprl\\gpprl\\all-small\\output"
    link.create_link_file(src_dir)
    print("Done.")


if __name__ == "__main__":
    test_create_link_file()

