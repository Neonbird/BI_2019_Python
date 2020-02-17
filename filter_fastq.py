#!/usr/bin/python
# -*- coding: UTF-8 -*-


import argparse


# count gc content of sequence
def gc_content(seq: str):
    gc = seq.count('G') + seq.count('C')
    return (gc / len(seq)) * 100


parser = argparse.ArgumentParser()
parser.add_argument('--min_length', default=1, type=int)
parser.add_argument('--keep_filtered', action="store_true")
parser.add_argument('--gc_bounds', type=int, nargs='*')
parser.add_argument('--output_base_name', type=str)
parser.add_argument('fastq')

args = parser.parse_args()

# create names for files with passed sequences and failed
if args.output_base_name:
    passed_filename = args.output_base_name + '__passed.fastq'
    failed_filename = args.output_base_name + '__failed.fastq'
else:
    passed_filename = args.fastq.replace(".fastq", "__passed.fastq")
    failed_filename = args.fastq.replace(".fastq", "__failed.fastq")

# create bounds for gc content if it is neсessary
if args.gc_bounds:
    if len(args.gc_bounds) == 1:
        min_gc = args.gc_bounds[0]
        max_gc = 100
    if len(args.gc_bounds) == 2:
        min_gc = args.gc_bounds[0]
        max_gc = args.gc_bounds[1]

# create file for failed reads if it is necessary; 
# if file with this name exits contents of the file are deleted
if args.keep_filtered:
    with open(failed_filename, "w") as file_failed:
        pass

# create file for passed reads; 
# if file with this name exits contents of the file are deleted
with open(passed_filename, "w") as file_passed:
    pass

with open(file=args.fastq) as file:
    for line in file:
        # find first read-specific line 
        # and remember this line and next 3 lines
        if line.startswith('@'):
            temp_lines = [line]
            for i in range(3):
                temp_lines.append(file.readline())
            # determine line with sequence
            seq = temp_lines[1]
            # check for length of read
            if len(seq) < args.min_length:
                # if lenght of read doesn't match 
                # write all 4 lines in file with failed reads 
                # if it is necessary
                if args.keep_filtered:
                    with open(failed_filename, "a") as file_failed:
                        for temp_line in temp_lines:
                            file_failed.write(temp_line)
                        file_failed.write('\n')
                # and come to next 4 lines
                continue
            # if it is necessary check for gc content of sequence
            elif args.gc_bounds:
                if gc_content(seq) > max_gc or gc_content(seq) < min_gc:
                    # if gc content of read doesn't match 
                    # write all 4 lines in file with failed reads 
                    # if it is necessary
                    if args.keep_filtered:
                        with open(failed_filename, "a") as file_failed:
                            for temp_line in temp_lines:
                                file_failed.write(temp_line)
                            file_failed.write('\n')
                    # and come to next 4 lines
                    continue
            # if all the requirements for the read are met, 
            # write all 4 lines to a file with passed reads
            with open(passed_filename, "a") as file_passed:
                for temp_line in temp_lines:
                    file_passed.write(temp_line)
                file_passed.write('\n')
