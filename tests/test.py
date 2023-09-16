# Don't run this file directly. The outer "test.py" needs to be the main script that runs,
# so that we can access the functionalities in "src/".
import unittest
import os
import src.main as main

current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)

class TestMainFunctionality(unittest.TestCase):

    def setUp(self):
        # copy the example file to the actual file that will be used
        with open(os.path.join(current_dir, "example_commit_dates.txt"), "r") as f:
            lines = f.readlines()
        
        with open("commit_dates.txt", "w") as f:
            f.writelines(lines)

    def test_main(self):
        # Run the main function
        main.main()

        # Read the expected output from example_filtered_commit_dates.txt
        with open(os.path.join(current_dir, "example_filtered_commit_dates.txt"), "r") as f:
            expected_data = f.read().strip()

        # Read the actual output from filtered_commit_dates.txt
        with open("filtered_commit_dates.txt", "r") as f:
            actual_data = f.read().strip()

        self.assertEqual(expected_data, actual_data)

    def tearDown(self):
        # Cleanup
        if os.path.exists("commit_dates.txt"):
            os.remove("commit_dates.txt")
        if os.path.exists("filtered_commit_dates.txt"):
            os.remove("filtered_commit_dates.txt")
