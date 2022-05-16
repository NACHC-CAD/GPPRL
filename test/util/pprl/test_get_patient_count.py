import main.util.file.file_util as fu
import main.util.pprl.get_number_of_patients as counter


def test_get_patient_count():
    print()
    print()
    print("Staring test...")
    zip_file_name = fu.get_file_name("test/resources/test-set-001/ymca.zip")
    print(counter.get_number_of_patients(zip_file_name))
    print("Done.")
