#!/usr/bin/env python
import os
import shutil
import re
import argparse
from modules import name_paste, parse_config, file_rip, pull_name, paste_file, clear_file

class Mp3Lib(object):
	def __init__(self):
		epilogue_text= "Please email the developer at joshwillik@gmail.com for further inquires"
		self.par = argparse.ArgumentParser(description="edit options in config file at ~/.py_mp3.conf", epilog=epilogue_text)
		self.par.add_argument('--version', action='version', version='%(prog)s v1.0.1')
		self.par.add_argument('-d','--default-config', help="reset config file to default", action='store_true') #implimented
		self.par.add_argument('-c', '--directory', help='specify working directory')
		self.par.add_argument('-r','--rip-file', help='pull metadata from file and paste in name',action='store_true')
		self.par.add_argument('-t','--pull-title', help="pull metadata from file name",action='store_true')
		self.par.add_argument('-p','--print-metadata',help="prints metadata specified in config", action='store_true')
		self.par.add_argument('-cl','--clear-metadata',help="clears all metadata from the file", action='store_true')
		self.opt= self.par.parse_args()
		# print self.opt #for debugging

		self.silented_pull = False #init var for use in pull_title
		self.pass_format_back = [] #init var for use in pull_title

		self.mp3_check = re.compile('\.mp3$') #regex object for checking if mp3 file
		self.hidden_dir = re.compile('^\..+$') #object for detecting hidden directories`
		self.file_repeat= re.compile('\(\d+\)\.') #object for dealing with duplicate filenames

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
			
			#set the different areas to get the data from, and give the data to
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
				self.pull_place = self.clear_metadata
				self.paste_place= self.null_function
			self.folder_crawl(self.opt.directory)
		elif not self.opt.directory:
			print "please specifiy directory"
		else:
			print "Unknown error, did you specify an operation?"

	def folder_crawl(self, directory):
		for root, sub_dir, files in os.walk(directory):
			for sub_sub_dir in sub_dir[:]:
				for i in re.findall(self.hidden_dir,sub_sub_dir): #remove hidden directories from folder_crawl
					sub_dir.remove(i) #this is to protect the .delete directory and custom hidden folders
			for specific in files:
				filename = os.path.join(root,specific) #create specific file name to give to modules
				file_root, extension = os.path.splitext(specific) #for checking filetype
				if re.search(self.mp3_check,specific): #check if mp3
					data = self.pull_place(filename) #pull from here
					self.paste_place(data, filename) #give to here
				elif extension in self.allowed_files: #if the file format is allowed, great, leave it
					pass
				else:
					self.move_to_delete(filename) #otherwise move to .delete
					print specific, " was moved to delete folder at: ", self.delete_dir

	def print_meta(self,file_data, filename):
		root, spec_filename = os.path.split(filename)
		del(file_data['-']) #remove the - from the file data. No-one wants to see that printed
		print "For file, ", spec_filename, ":" #print what the file is
		for i in file_data:
			print i,":",file_data[i] #print the data
		print "="*20 #seperator

	def move_to_delete(self, to_move,try_num=1):
		old_name = to_move #used to rename the file
		try:
			shutil.move(to_move, self.delete_dir) #move the file
			print "The file was moved, "
		except: #if a file of that name already exists
			root_of_file, extension = os.path.splitext(to_move) #add a (0) number identifier
			if try_num == 1: #if this is the first time the error happens
				to_move = root_of_file + "("+str(try_num)+")" + extension #just add an identifier
			else:
				begin, re_extension = re.split(self.file_repeat, to_move) #otherwise insert a custom identifier
				to_move = begin + "("+str(try_num)+")."+re_extension
			#print to_move #for debugging
			os.rename(old_name, to_move) #rename file to valid name
			self.move_to_delete(to_move,try_num+1) #attempt to move the file again, with a higher try number for renaming
		try_num+=1 #probably exists for previous attempt at this functionality. Most likely redundant
	def rip_file(self, filename):
		ripped_file = file_rip.Ripper(filename) #set file for ripping
		ripped_data = ripped_file.song_data #take data 
		return ripped_data #return it
	def clear_metadata(self,filename):
		cleared_file = clear_file.Clearer(filename) #give filename to clearing module
	def paste_file(self,file_data,filename):
		pasted_file = paste_file.Paster(file_data, filename) #give filename and file data for pasting into the file
	def paste_name(self,file_data,filename):
		name_paste.Paster(file_data,self.parsed_array,filename) #give filename and file data for pasting into name
	def pull_name(self,filename):
		pulled_data = pull_name.Puller(filename, self.silented_pull,self.pass_format_back) #run the first time
		ripped_data = pulled_data.name_data #get data
		self.silented_pull = pulled_data.pickup_answer #check for successful execution and silence next run
		self.pass_format_back = pulled_data.end_format #check for format and silence future question asking
		return ripped_data #return data
	def parse_config(self):
		temp_obj = parse_config.Parser() #run the object
		self.parsed_array = temp_obj.parsed #take config array
		self.allowed_files= temp_obj.allowed_files #take extra allowed files

	def null_function(self, null = None, renull = None, more_null = None): #used to make the clear file function fit
		pass


start = Mp3Lib() #start the program off
