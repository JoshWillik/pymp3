class Parser(object):
	def __init__(self):
		self.names  = ['discnumber','tracknumber','artist','title','album', '-']
		self.config = os.path.expanduser('~/.py_mp3.conf')
		if not os.path.exists(self.config):
			self.init_config()
		else:
			self.parse()


	def init_config(self):
		create_config = open(self.config, 'w')
		create_config.write("discnumber.tracknumber - artist - title\n")
		create_config.write("#options: discnumber, tracknumber, artist, title, album\n")
		create_config.write('#use spaces to separate items, periods to signify non-space seperators\n')
		create_config.close()
		print "####################################\nConfig file generated at: ",self.config+"\n####################################"
		self.parse()

	def parse(self):
		to_parse = open(self.config)
		parsed = to_parse.readline().split()
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
		print self.parsed

if __name__ == "__main__":
	import os
	start = Parser()
