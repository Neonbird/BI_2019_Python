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

    def test_dont_create_failed_file(self):
        args_keep_filtered = None
        failed_filename = "i_should_exist__failed.fastq"
        filtering.create_file(failed_filename, args_keep_filtered)
        self.assertFalse(path.exists(failed_filename))
        self.silent_remove(failed_filename)

    def test_create_failed_file(self):
        args_keep_filtered = True
        failed_filename = "i_should_exist__failed.fastq"
        filtering.create_file(failed_filename, args_keep_filtered)
        self.assertTrue(path.exists(failed_filename))
        self.silent_remove(failed_filename)

    def test_create_passed_file(self):
        passed_filename = 'filename__passed.fastq'
        filtering.create_file(passed_filename, True)
        self.assertTrue(path.exists(passed_filename))
        self.silent_remove(passed_filename)


if __name__ == '__main__':
    unittest.main()
