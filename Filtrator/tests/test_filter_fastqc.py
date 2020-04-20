import unittest
import Filtrator.filter_fastq_modified as filtering
from os import path, remove


class TestFilterFastqc(unittest.TestCase):
    def silent_remove(self, filename):
        try:
            self.addCleanup(remove, filename)
        except FileNotFoundError:
            pass

    def test_gc_content(self):
        self.assertEqual(50, filtering.gc_content("GCGAAT"))
        self.assertEqual(0, filtering.gc_content("TAAAT"))
        self.assertEqual(100, filtering.gc_content("GCGGGC"))

    def test_output_base_name_arg_true(self):
        args_fastq = "defolt_name.fastq"
        args_output_base_name = 'good'
        result = filtering.make_output_filenames(args_output_base_name, args_fastq)
        self.assertEqual(result, ('good__passed.fastq', 'good__failed.fastq'))

    def test_output_base_name_arg_false(self):
        args_fastq = "defolt_name.fastq"
        self.args_output_base_name = None
        result = filtering.make_output_filenames(None, args_fastq)
        self.assertEqual(result, ('defolt_name__passed.fastq', 'defolt_name__failed.fastq'))

    def test_create_gc_bounds_no_bounds(self):
        args_gc_bounds = None
        self.assertEqual((0, 100), filtering.create_gc_bounds(args_gc_bounds))

    def test_create_gc_bounds_one_bound(self):
        args_gc_bounds = [30]
        self.assertEqual((30, 100), filtering.create_gc_bounds(args_gc_bounds))

    def test_create_gc_bounds_two_bounds(self):
        args_gc_bounds = [30, 50]
        self.assertEqual((30, 50), filtering.create_gc_bounds(args_gc_bounds))

    def test_create_output_file(self):
        filename = "i_should_exist.fastq"
        filtering.create_file(filename)
        self.assertTrue(path.exists(filename))
        self.silent_remove(filename)


if __name__ == '__main__':
    unittest.main()
