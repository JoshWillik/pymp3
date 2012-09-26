#!/usr/bin/env python
import os
import argparse

par = argparse.ArgumentParser(description="A foo that bars", epilog='a bar that foos')
par.add_argument('-c','--directory')
par.add_argument('-o','--output-log')
par.add_argument('--version', action='version', version='%(prog)s v0.0.1')
par.add_argument('-r','--rip-')
par.add_argument('-t','--pull-title')
par.add_argument('-p','--print-metadata', action='store_true')
opt= par.parse_args()
#print opt

def main():
	directory = get_directory(opt.directory)
	print directory
	output_log = set_log_out(opt.output_log)
	print output_log
	if(opt.print_metadata):
		print_folder_metadata(directory)


def get_directory(path):
	#print os.path.abspath(opt.directory)
	if(path):
		return os.path.abspath(path)
	else:
		return False


def set_log_out(path):
	if(path):
		return os.path.abspath(path)
	else:
		return False

def print_folder_metadata(directory):
	for i in directory:
		print i

if __name__ == '__main__':
	main()
