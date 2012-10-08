#!/usr/bin/env python
import os
import argparse
from modules import name_paste, parse_config, file_rip

class Mp3Lib(object):
	def __init__(self):
		epilogue_text= "Please email the developer at joshwillik@gmail.com for further inquires"
		self.par = argparse.ArgumentParser(description="Will generate a config file in ~/.py_mp3.conf", epilog=epilogue_text)
		self.par.add_argument('--version', action='version', version='%(prog)s v0.0.1')
		self.par.add_argument('-d','--default-config', help="Reset config file to default", action='store_true')
		self.par.add_argument('directory',help='specify working directory')
		self.par.add_argument('-r','--rip', help='pull metadata from file and paste in name')
		self.par.add_argument('-t','--pull-title', help="^^in development^^")
		self.par.add_argument('-p','--print-metadata', action='store_true')
		self.opt= self.par.parse_args()
		print self.opt
		if self.opt.default_config:
			os.remove(os.path.expanduser("~/.py_mp3.conf"))
			self.parse_config()
		if self.opt.print_metadata:
			self.print_folder(self.opt.directory)

	def print_folder(self, directory):
		print "folder"
	def rip_data(self):
		print "lawl"
	def pull_name(self):
		print "leedle"
	def parse_config(self):
		
		parseconfig.Parser()

start = Mp3Lib()