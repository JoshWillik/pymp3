class Parser(object):
	def __init__(self):
		import os
		self.names  = ['discnumber','tracknumber','artist','title','album', '-'] #list of valid inputs
		self.config = os.path.expanduser('~/.pymp3.conf') #path to config file
		if not os.path.exists(self.config):
			self.init_config() #initiate config file if it doesn't exist
		else:
			self.parse()


	def init_config(self):
		create_config = open(self.config, 'w')
		create_config.write("discnumber.tracknumber - artist - title\n")
		create_config.write("\n") #creates space for other allowed file formats
		create_config.write("#only lines 1 and 2 are parsed\n")
		create_config.write("#line 1 options: discnumber, tracknumber, artist, title, album\n")
		create_config.write('#use spaces to separate items, periods to signify non-space seperators\n')
		create_config.write('#dashes, "-", show up as dashes.\n')
		create_config.write('#line 2 options: any file extension.\n')
		create_config.write('#remember to include spaces and put a . before each\n')
		create_config.write('#ex: .m4a .flac .jpg .png\n')
		create_config.write('#this will make the script skip m4a, flac, jpg, and png files\n')
		create_config.close()

		#generation message 
		print "####################################\nConfig file generated at: ",self.config+"\n####################################"
		self.parse()

	def parse(self):
		to_parse = open(self.config)
		parsed = to_parse.readline().split() #read output format
		if parsed == []:
			raise Exception("Parse line empty")
		for i in range(0, len(parsed)):
			parsed[i] = parsed[i].split('.')
		for i in parsed:
		 	if type(i) == list:
		 		for y in i:
		 			if not y in self.names:
		 				raise Exception('InvalidParseName', "Please check "+self.config+" for errors.")
			else:
				if not i in self.names:
					raise Exception('InvalidParseName')
		self.parsed = parsed
		print "\nFormat pulled from ",self.config, "is\n",self.parsed
		allowed = to_parse.readline().split()
		self.allowed_files = allowed
		if allowed == []:
			print "No extra file formats allowed"
		else:
			print "Extra formats: ", allowed
		to_parse.close()

if __name__ == "__main__":
	#modules not designed to function independantly, for testing purposes only
	start = Parser()
