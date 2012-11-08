class Paster(object):
	def __init__(self, song_data, parse_array,target_file):
		import os
		import re

		#make variables module wide
		self.re = re
		self.os = os
		self.song_data = song_data
		self.parse_array = parse_array
		self.target_file = target_file
		self.song_data = song_data
		self.parse_array = parse_array
		self.main()

	def main(self):
		new_name = ""
		for i in range(0,len(self.parse_array)): #for every item in the outer array
			for y in self.parse_array[i]: #in case the item is an array, which should be joined without spaces
				if y != "-":
					new_name += self.song_data[y]
				else:
					new_name += "-"
			new_name += " "

		new_name=new_name.strip()
		new_name+=".mp3"
		new_name = self.re.compile('[^\w\"\' -\.]').sub("",new_name) #clear special characters from the name
		#rename file to new name
		self.os.rename(self.target_file, self.os.path.join(self.os.path.dirname(self.os.path.abspath(self.target_file)),new_name))



if __name__ == "__main__":
	#modules not designed to function independantly, for testing purposes only
	import os
	
	#get parsed configuration data to pass to name paster
	import parse_config
	parsed_config = parse_config.Parser()
	parse_format = parsed_config.parsed

	#get filename to pass to file renamer
	from sys import argv
	try:
		target = argv[1]
	except IndexError:
		raise Exception("no target file specified")
	script = argv[0]

	#get song data to pass to file renamer
	import file_rip
	ripped = file_rip.Ripper(target).song_data
	start_paste = Paster(ripped, parse_format, target)