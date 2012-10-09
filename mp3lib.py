#!/usr/bin/env python
import os
import shutil
import re
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

		self.mp3_check = re.compile('\.mp3$') #regex object for checking if mp3 file
		self.hidden_dir = re.compile('^\..+$') #object for detecting hidden directories`

		if not os.path.exists(self.opt.directory):
			raise Exception("Invalid directory")
		elif not os.access(self.opt.directory, os.W_OK): #check for write access to directory
			raise Exception("Access to directory permitted")
		else:
			if not os.path.exists(os.path.join(self.opt.directory, '.delete')): 
				os.mkdir(os.path.join(self.opt.directory, '.delete')) #store files cued for deletion
			self.delete_dir = os.path.join(self.opt.directory, '.delete')

		if self.opt.default_config:
			os.remove(os.path.expanduser("~/.py_mp3.conf"))
			self.parse_config()
		else:
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
		else:
			print "Unknown error"

	def folder_crawl(self, directory):
		for root, sub_dir, files in os.walk(directory):
			for sub_sub_dir in sub_dir[:]:
				for i in re.findall(self.hidden_dir,sub_sub_dir):
					sub_dir.remove(i)
			for specific in files:
				filename = os.path.join(root,specific)
				if re.search(self.mp3_check,specific):
					data = self.pull_place(filename)
					self.paste_place(data, filename)
				else:
					self.move_to_delete(filename)
					print specific, " was moved to delete folder at: ", self.delete_dir

	def print_meta(self,file_data, filename):
		print "file data is: ", file_data
		print "file path is: ", filename
	def move_to_delete(self, to_move, try_num=1):
		print 'start directory', to_move
		try:
			shutil.move(to_move, self.delete_dir)
		except:
			if try_num ==1:
				to_move = "("+str(try_num)+")"+to_move
			else:
				root_of_file, extension = os.path.splitext(to_move)
				to_move = root_of_file + "("+str(try_num)+")" + extension
				print to_move
				move_to_delete(to_move,try_num+1)
		try_num+=1
	def rip_file(self, filename):
		ripped_data = file_rip.Ripper(filename).song_data
		return ripped_data
	def paste_file(self,file_data,filename):
		print "file data is: ", file_data
		print "file path is: ", filename
	def paste_name(self,file_data,filename):
		name_paste.Paster(file_data,self.parsed_array,filename)
	def pull_name(self,filename):
		print "file path is: ", filename
	def parse_config(self):
		self.parsed_array = parse_config.Parser().parsed

start = Mp3Lib()