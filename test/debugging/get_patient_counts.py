import main.util.pprl.get_number_of_patients as counter


def test_get_number_of_patients():
    print()
    print()
    print("Starting test...")
    src_dir = "D:\\test\\pprl\\linkage-agent-scaling-test-set-2\\_SRC"
    counter.get_number_of_patients_for_dir(src_dir)
    print("Done.")

