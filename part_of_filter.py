import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--output_base_name', type=str)
args = parser.parse_args()


''' 
Create names for files with passed sequences and failed
'''
def check_output_base_name(args_output_base_name):
    # if True
    if args_output_base_name:
        passed_filename = args.output_base_name + '__passed.fastq'
        failed_filename = args.output_base_name + '__failed.fastq'
    else:
        passed_filename = args.fastq.replace(".fastq", "__passed.fastq")
        failed_filename = args.fastq.replace(".fastq", "__failed.fastq")
    return (passed_filename, failed_filename)