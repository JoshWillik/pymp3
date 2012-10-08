#!/usr/bin/env python
import os
import argparse
from modules import name_paste, parse_config, file_rip

class Mp3Lib(object):
	def __init__(self):
		epilogue_text= "Please email the developer at joshwillik@gmail.com for further inquires"
		self.par = argparse.ArgumentParser(description="edit options in config file at ~/.py_mp3.conf", epilog=epilogue_text)
		self.par.add_argument('--version', action='version', version='%(prog)s v0.0.1')
		self.par.add_argument('-d','--default-config', help="Reset config file to default", action='store_true') #implimented
		self.par.add_argument('-c', '--directory', help='specify working directory')
		self.par.add_argument('-r','--rip-file', help='pull metadata from file and paste in name',action='store_true')
		self.par.add_argument('-t','--pull-title', help="pull metadata from file name^^in development^^",action='store_true')
		self.par.add_argument('-p','--print-metadata',help="prints metadata specified in config", action='store_true')
		self.opt= self.par.parse_args()
		# print self.opt #for debugging
		if self.opt.default_config:
			os.remove(os.path.expanduser("~/.py_mp3.conf"))
			self.parse_config()
		if (self.opt.pull_title and self.opt.rip_file) or (self.opt.pull_title and self.opt.print_metadata) or (self.opt.rip_file and self.opt.print_metadata):
			print "Invalid combination of options"
			print "Please select rip-file OR pull-title, not both"
		elif (self.opt.print_metadata or self.opt.pull_title or self.opt.rip_file) and self.opt.directory:
			if self.opt.print_metadata:
				self.pull_place = self.rip_file
				self.paste_place= self.print_meta
			elif self.opt.pull_title:
				self.pull_place = self.pull_name
				self.paste_place= self.paste_file
			elif self.opt.rip_file:
				self.pull_place = self.rip_file
				self.paste_place= self.paste_name
			self.folder_crawl(self.opt.directory)
		elif not self.opt.directory:
			print "please specifiy directory"

	def folder_crawl(self, directory):
		for root, sub_dir, files in os.walk(directory):
			for specific in files:
				filename = os.path.join(root,specific)
				data = self.pull_place(filename)
				self.paste_place(data, filename)

	def print_meta(self,file_data, filename):
		print "file data is: ", file_data
		print "file path is: ", filename
	def rip_file(self, filename):
		print "file path is: ", filename
	def paste_file(self,file_data,filename):
		print "file data is: ", file_data
		print "file path is: ", filename
	def paste_name(self,file_data,filename):
		print "file data is: ", file_data
		print "file path is: ", filename
	def pull_name(self,filename):
		print "file path is: ", filename
	def parse_config(self):
		parseconfig.Parser()

start = Mp3Lib()