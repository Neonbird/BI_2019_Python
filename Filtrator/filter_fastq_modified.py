#!/usr/bin/python
# -*- coding: UTF-8 -*-


import argparse


# count gc content of sequence
def gc_content(seq: str):
    gc = seq.count('G') + seq.count('C')
    return (gc / len(seq)) * 100


# Create names for files with passed sequences and failed
def make_output_filenames(args_output_base_name, args_fastq):
    if args_output_base_name:
        passed_filename = args_output_base_name + '__passed.fastq'
        failed_filename = args_output_base_name + '__failed.fastq'
    else:
        passed_filename = args_fastq.replace(".fastq", "__passed.fastq")
        failed_filename = args_fastq.replace(".fastq", "__failed.fastq")
    return (passed_filename, failed_filename)


# create bounds for gc content if it is neсessary
def create_gc_bounds(args_gc_bounds):
    if args_gc_bounds:
        if len(args_gc_bounds) == 1:
            min_gc = args_gc_bounds[0]
            max_gc = 100
        if len(args_gc_bounds) == 2:
            min_gc = args_gc_bounds[0]
            max_gc = args_gc_bounds[1]
    else:
        min_gc, max_gc = 0, 100
    return(min_gc, max_gc)


# create file;
# if file with this name exits contents of the file are deleted
def create_file(filename):
    with open(filename, "w") as _:
        pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--min_length', type=int)
    parser.add_argument('--keep_filtered', action="store_true")
    parser.add_argument('--gc_bounds', type=int, nargs='*')
    parser.add_argument('--output_base_name', type=str)
    parser.add_argument('fastq')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    passed_filename, failed_filename = make_output_filenames(args.output_base_name, args.fastq)
    min_gc, max_gc = create_gc_bounds(args.gc_bounds)
    create_file(passed_filename)
    if args.keep_filtered:
        create_file(failed_filename)
    with open(args.fastq) as file:
        for line in file:
            # take info about one read
            temp_lines = [line, next(file), next(file), next(file)]
            seq = temp_lines[1]
            # check for length of read
            if (len(seq) - 1) < args.min_length:
                # if lenght of read doesn't match
                # write all 4 lines in file with failed reads
                # if it is necessary
                if args.keep_filtered:
                    with open(failed_filename, "a") as file_for_failed_reads:
                        for temp_line in temp_lines:
                            file_for_failed_reads.write(temp_line)
                    # and come to next 4 lines
                    continue
                # if it is necessary check for gc content of sequence
            elif args.gc_bounds:
                if gc_content(seq) > max_gc or gc_content(seq) < min_gc:
                    # if gc content of read doesn't match
                    # write all 4 lines in file with failed reads
                    # if it is necessary
                    if args.keep_filtered:
                        with open(failed_filename, "a") as file_for_failed_reads:
                            for temp_line in temp_lines:
                                file_for_failed_reads.write(temp_line)
                        # and come to next 4 lines
                        continue
            # if all the requirements for the read are met,
            # write all 4 lines from temp to a file with passed reads
            with open(passed_filename, "a") as file_passed:
                for temp_line in temp_lines:
                    file_passed.write(temp_line)
