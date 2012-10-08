class Parser(object):
	def __init__(self):
		self.config = os.path.expanduser('~/.py_mp3.conf')
		if not os.path.exists(self.config):
			self.init_config()
		else:
			self.parse()

	def init_config(self):
		create_config = open(self.config, 'w')
		create_config.write("cd_num.track_num - artist - title\n")
		create_config.write("#options: discnumber, tracknumber, artist, title, album\n")
		create_config.write('#use spaces to seperate items, periods to signify non-space seperators\n')
		create_config.close()
		print "####################################\nConfig file generated at: ",self.config+"\n####################################"
		self.parse()

	def parse(self):
		to_parse = open(self.config)
		parsed = to_parse.readline().split()
		for i in range(0, len(parsed)):
			parsed[i] = parsed[i].split('.')
		self.parsed = parsed
		print self.parsed

if __name__ == "__main__":
	import os
	start = Parser()
