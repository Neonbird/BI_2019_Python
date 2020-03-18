import unittest
import argparse
from filt import check_output_base_name


class TestFilterFastqc(unittest.TestCase):

    def setUp(self) -> None:
        parser = argparse.ArgumentParser()
        parser.add_argument('--min_length', default=1, type=int)
        parser.add_argument('--keep_filtered', action="store_true")
        parser.add_argument('--gc_bounds', type=int, nargs='*')
        parser.add_argument('--output_base_name', type=str)
        parser.add_argument('fastq')
        self.args = parser.parse_args()

    def test_output_base_name_arg_true(self):
        self.args.fastq = "defolt_name.fastq"
        self.args.output_base_name = 'good'
        result = check_output_base_name(self.args.output_base_name)
        self.assertEqual(result, ('good__passed.fastq', 'good__failed.fastq'))

    def test_output_base_name_arg_false(self):
        self.args.fastq = "defolt_name.fastq"
        # self.args.output_base_name = 'good'
        result = check_output_base_name(self.args.output_base_name)
        self.assertEqual(result, ('defolt_name__passed.fastq', 'defolt_name__failed.fastq'))


if __name__ == '__main__':
    unittest.main()

# tearDown()