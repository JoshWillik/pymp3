import os
import argparse

class Mp3Lib(object):
	def __init__(self):
		try:
			os.path.isfile("~/mp3morph.conf")
		except:
			#CREATE mp3morph.conf
		self.par = argparse.ArgumentParser(description="A foo that bars", epilog='a bar that foos')
		self.par.add_argument('-c','--directory')
		self.par.add_argument('-o','--output-log')
		self.par.add_argument('--version', action='version', version='%(prog)s v0.0.1')
		self.par.add_argument('-r','--rip-')
		self.par.add_argument('-t','--pull-title')
		self.par.add_argument('-p','--print-metadata', action='store_true')
		self.opt= self.par.parse_args()
		print self.par,"+++", self.opt
	def print_folder(self):
		continue

	def rip_data(self):
		continue

	def pull_name(self):
		continue

