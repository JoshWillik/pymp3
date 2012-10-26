#!/usr/bin/env python
import os
import shutil
import re
import argparse
from modules import name_paste, parse_config, file_rip, pull_name

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
		self.par.add_argument('-cl','--clear-metadata',help="clears all metadata from the file", action='store_true')
		self.opt= self.par.parse_args()
		# print self.opt #for debugging

		self.mp3_check = re.compile('\.mp3$') #regex object for checking if mp3 file
		self.hidden_dir = re.compile('^\..+$') #object for detecting hidden directories`

		if self.opt.default_config:
			if os.path.exists(os.path.expanduser("~/.py_mp3.conf")):
				os.remove(os.path.expanduser("~/.py_mp3.conf"))
			self.parse_config()
			raise Exception("Default configuration restored")
		else:
			self.parse_config()

		if not os.path.exists(self.opt.directory):
			raise Exception("Invalid directory")
		elif not os.access(self.opt.directory, os.W_OK): #check for write access to directory
			raise Exception("Access to directory permitted")
		else:
			if not os.path.exists(os.path.join(self.opt.directory, '.delete')): 
				os.mkdir(os.path.join(self.opt.directory, '.delete')) #store files cued for deletion
			self.delete_dir = os.path.join(self.opt.directory, '.delete')

		if (self.opt.pull_title and self.opt.rip_file)\
		 or (self.opt.pull_title and self.opt.print_metadata)\
		  or (self.opt.rip_file and self.opt.print_metadata)\
		  or (self.opt.clear_metadata and self.opt.print_metadata)\
		  or (self.opt.clear_metadata and self.opt.pull_title)\
		  or (self.opt.clear_metadata and self.opt.rip_file):
			print "Invalid combination of options"
			print "Please select rip-file OR pull-title, not both"
		elif (self.opt.print_metadata or self.opt.pull_title or self.opt.rip_file or self.opt.clear_metadata) and self.opt.directory:
			if self.opt.print_metadata:
				self.pull_place = self.rip_file
				self.paste_place= self.print_meta
			elif self.opt.pull_title:
				self.pull_place = self.pull_name
				self.paste_place= self.paste_file
			elif self.opt.rip_file:
				self.pull_place = self.rip_file
				self.paste_place= self.paste_name
			elif self.opt.clear_metadata:
				self.pull_place = self.rip_file
				self.paste_place= self.clear_metadata
			self.folder_crawl(self.opt.directory)
		elif not self.opt.directory:
			print "please specifiy directory"
		else:
			print "Unknown error, did you specify an operation?"

	def folder_crawl(self, directory):
		for root, sub_dir, files in os.walk(directory):
			for sub_sub_dir in sub_dir[:]:
				for i in re.findall(self.hidden_dir,sub_sub_dir):
					sub_dir.remove(i)
			for specific in files:
				filename = os.path.join(root,specific)
				file_root, extension = os.path.splitext(specific)
				if re.search(self.mp3_check,specific):
					data = self.pull_place(filename)
					self.paste_place(data, filename)
				elif extension in self.allowed_files:
					pass
				else:
					self.move_to_delete(filename)
					print specific, " was moved to delete folder at: ", self.delete_dir

	def print_meta(self,file_data, filename):
		root, spec_filename = os.path.split(filename)
		del(file_data['-'])
		print "For file, ", spec_filename, ":"
		for i in file_data:
			print i,":",file_data[i]
		print "="*10

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
		self.rip_file = file_rip.Ripper(filename)
		ripped_data = self.rip_file.song_data
		return ripped_data
	def clear_metadata(self,use,less):
		self.rip_file.clear()
	def paste_file(self,file_data,filename):
		print "file data is: ", file_data
		print "file path is: ", filename
	def paste_name(self,file_data,filename):
		name_paste.Paster(file_data,self.parsed_array,filename)
	def pull_name(self,filename):
		print "file path is: ", filename
	def parse_config(self):
		temp_obj = parse_config.Parser()
		self.parsed_array = temp_obj.parsed
		self.allowed_files= temp_obj.allowed_files


start = Mp3Lib()
