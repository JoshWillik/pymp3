class Paster(object):
	def __init__(self, song_data, parse_array,target_file):
		import os
		self.song_data = song_data
		self.parse_array = parse_array
		self.main()
	def main(self):
		new_name = ""
		for i in range(0,len(self.parse_array)):
			for y in self.parse_array[i]:
				new_name += self.song_data[y]
			new_name += " "
		new_name=new_name.strip()
		new_name+=".mp3"
		print new_name
		os.rename(target, os.path.dirname(os.path.abspath(target))+"/"+new_name)



if __name__ == "__main__":
	#NOTE: "__main__" for debugging purposes only, not meant to be used individually
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